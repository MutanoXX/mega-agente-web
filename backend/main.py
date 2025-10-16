from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, Dict
import json
import os

from agent import PollinationsAgent

app = FastAPI(title="Mega Agent API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,  # No cookies/auth, so False is safer
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global agent instance
agent = PollinationsAgent()


class ChatRequest(BaseModel):
    message: str
    models: Optional[Dict[str, str]] = None


class ModelsResponse(BaseModel):
    text_models: list
    search_models: list
    reasoning_models: list
    image_models: list
    audio_voices: list


@app.get("/api")
async def api_info():
    """API information endpoint"""
    return {
        "message": "Mega Agent API - Powered by Pollinations.AI",
        "version": "1.0.0",
        "endpoints": {
            "/chat": "POST - Send a message to the agent (streaming)",
            "/models": "GET - Get available models",
            "/clear": "POST - Clear conversation history"
        }
    }


@app.get("/models", response_model=ModelsResponse)
async def get_models():
    """Get all available models"""
    return ModelsResponse(
        text_models=PollinationsAgent.TEXT_MODELS,
        search_models=PollinationsAgent.SEARCH_MODELS,
        reasoning_models=PollinationsAgent.REASONING_MODELS,
        image_models=PollinationsAgent.IMAGE_MODELS,
        audio_voices=PollinationsAgent.AUDIO_VOICES
    )


@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Chat with the agent (streaming response)
    """
    async def event_generator():
        try:
            async for event in agent.process_message_stream(
                request.message,
                request.models
            ):
                yield f"data: {json.dumps(event)}\n\n"
        except Exception as e:
            error_event = {
                "type": "error",
                "message": str(e)
            }
            yield f"data: {json.dumps(error_event)}\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


@app.post("/clear")
async def clear_history():
    """Clear conversation history"""
    agent.clear_history()
    return {"message": "Conversation history cleared"}


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    await agent.close()


# Mount static files (frontend)
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

import httpx
import json
import asyncio
from typing import AsyncGenerator, Dict, List, Optional, Any
from enum import Enum


class ToolType(Enum):
    """Available tool types for the agent"""
    TEXT_GENERATION = "text_generation"
    IMAGE_GENERATION = "image_generation"
    SEARCH = "search"
    TEXT_TO_SPEECH = "text_to_speech"
    SPEECH_TO_TEXT = "speech_to_text"
    VISION = "vision"
    REASONING = "reasoning"


class PollinationsAgent:
    """
    Mega Agent that uses all Pollinations.AI capabilities
    """
    
    BASE_URL_TEXT = "https://text.pollinations.ai"
    BASE_URL_IMAGE = "https://image.pollinations.ai"
    
    # Available models by category
    TEXT_MODELS = ["openai", "openai-fast", "mistral", "claude"]
    SEARCH_MODELS = ["searchgpt"]
    REASONING_MODELS = ["openai-reasoning", "openai"]
    IMAGE_MODELS = ["flux", "flux-realism", "flux-anime", "flux-3d", "turbo"]
    AUDIO_VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=300.0)
        self.conversation_history: List[Dict] = []
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()
    
    def _determine_tool(self, user_message: str) -> ToolType:
        """
        Analyze user message to determine which tool to use
        """
        message_lower = user_message.lower()
        
        # Check for image generation keywords
        image_keywords = ["imagem", "desenhe", "crie uma imagem", "gere uma imagem", "picture", "draw", "image", "foto", "ilustração"]
        if any(keyword in message_lower for keyword in image_keywords):
            return ToolType.IMAGE_GENERATION
        
        # Check for search keywords
        search_keywords = ["pesquise", "busque", "procure", "search", "find", "latest", "news", "notícias", "o que está acontecendo"]
        if any(keyword in message_lower for keyword in search_keywords):
            return ToolType.SEARCH
        
        # Check for audio generation keywords
        audio_keywords = ["fale", "diga", "áudio", "voz", "speak", "say", "audio", "voice"]
        if any(keyword in message_lower for keyword in audio_keywords):
            return ToolType.TEXT_TO_SPEECH
        
        # Vision is not yet implemented, so we skip these keywords for now
        # vision_keywords = ["analise esta imagem", "o que tem nesta imagem", "descreva a imagem", "analyze image", "what's in this image"]
        # if any(keyword in message_lower for keyword in vision_keywords):
        #     return ToolType.VISION
        
        # Check for reasoning keywords
        reasoning_keywords = ["pense", "raciocine", "analise profundamente", "think", "reason", "analyze deeply", "complexo"]
        if any(keyword in message_lower for keyword in reasoning_keywords):
            return ToolType.REASONING
        
        # Default to text generation
        return ToolType.TEXT_GENERATION
    
    async def generate_text_stream(
        self,
        prompt: str,
        model: str = "openai",
        system_prompt: Optional[str] = None,
        temperature: float = 0.7
    ) -> AsyncGenerator[str, None]:
        """
        Generate text with streaming using Pollinations.AI
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        # Add conversation history
        messages.extend(self.conversation_history[-6:])  # Last 3 exchanges
        
        # Add current user message
        messages.append({"role": "user", "content": prompt})
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "stream": True
        }
        
        async with self.client.stream(
            "POST",
            f"{self.BASE_URL_TEXT}/openai",
            json=payload,
            headers={"Content-Type": "application/json", "Accept": "text/event-stream"}
        ) as response:
            # Check for HTTP errors
            if response.status_code != 200:
                error_text = await response.aread()
                raise Exception(f"API error {response.status_code}: {error_text.decode()}")
            
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    data = line[6:]
                    if data.strip() == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        content = chunk.get("choices", [{}])[0].get("delta", {}).get("content")
                        if content:
                            yield content
                    except json.JSONDecodeError:
                        continue
    
    async def generate_image(
        self,
        prompt: str,
        model: str = "flux",
        width: int = 1024,
        height: int = 1024,
        seed: Optional[int] = None
    ) -> str:
        """
        Generate an image and return its URL
        """
        params = {
            "model": model,
            "width": width,
            "height": height,
            "nologo": "true"
        }
        
        if seed:
            params["seed"] = seed
        
        # URL encode the prompt and construct the image URL
        # The frontend will trigger the actual generation
        from urllib.parse import quote, urlencode
        encoded_prompt = quote(prompt)
        
        # Build query string
        query_string = urlencode(params)
        url = f"{self.BASE_URL_IMAGE}/prompt/{encoded_prompt}?{query_string}"
        
        return url
    
    async def search_web(
        self,
        query: str,
        model: str = "searchgpt"
    ) -> AsyncGenerator[str, None]:
        """
        Search the web using SearchGPT model via POST endpoint for consistent streaming
        """
        messages = [{"role": "user", "content": query}]
        
        payload = {
            "model": model,
            "messages": messages,
            "stream": True
        }
        
        async with self.client.stream(
            "POST",
            f"{self.BASE_URL_TEXT}/openai",
            json=payload,
            headers={"Content-Type": "application/json", "Accept": "text/event-stream"}
        ) as response:
            # Check for HTTP errors
            if response.status_code != 200:
                error_text = await response.aread()
                raise Exception(f"API error {response.status_code}: {error_text.decode()}")
            
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    data = line[6:]
                    if data.strip() == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        content = chunk.get("choices", [{}])[0].get("delta", {}).get("content")
                        if content:
                            yield content
                    except json.JSONDecodeError:
                        continue
    
    def _extract_text_for_tts(self, user_message: str) -> str:
        """
        Extract the actual text to speak, removing trigger words
        """
        message_lower = user_message.lower()
        
        # Common trigger patterns
        triggers = [
            ("fale:", "fale:"),
            ("diga:", "diga:"),
            ("speak:", "speak:"),
            ("say:", "say:"),
            ("fale ", "fale "),
            ("diga ", "diga "),
            ("speak ", "speak "),
            ("say ", "say "),
        ]
        
        for trigger_lower, trigger_original in triggers:
            if trigger_lower in message_lower:
                # Find the position and extract text after it
                idx = message_lower.find(trigger_lower)
                text = user_message[idx + len(trigger_original):].strip()
                if text:
                    return text
        
        # If no trigger found, return original message
        return user_message
    
    async def generate_audio_url(
        self,
        text: str,
        voice: str = "nova"
    ) -> str:
        """
        Generate audio and return its URL
        """
        from urllib.parse import quote
        
        # Extract actual text to speak (remove trigger words)
        clean_text = self._extract_text_for_tts(text)
        encoded_text = quote(f"Say verbatim: {clean_text}")
        
        url = f"{self.BASE_URL_TEXT}/{encoded_text}"
        params = {
            "model": "openai-audio",
            "voice": voice
        }
        
        # The URL itself is the audio endpoint
        return f"{url}?model={params['model']}&voice={params['voice']}"
    
    async def process_message_stream(
        self,
        user_message: str,
        selected_models: Optional[Dict[str, str]] = None
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Process user message and stream responses with tool information
        """
        # Determine which tool to use
        tool_type = self._determine_tool(user_message)
        
        # Get selected models or use defaults
        models = selected_models or {}
        text_model = models.get("text", "openai")
        search_model = models.get("search", "searchgpt")
        reasoning_model = models.get("reasoning", "openai-reasoning")
        image_model = models.get("image", "flux")
        audio_voice = models.get("audio", "nova")
        
        # Emit tool selection
        tool_names = {
            ToolType.TEXT_GENERATION: "💬 Geração de Texto",
            ToolType.IMAGE_GENERATION: "🎨 Geração de Imagem",
            ToolType.SEARCH: "🔍 Pesquisa Web",
            ToolType.TEXT_TO_SPEECH: "🔊 Text-to-Speech",
            ToolType.REASONING: "🧠 Raciocínio Avançado",
            ToolType.VISION: "👁️ Análise de Imagem"
        }
        
        yield {
            "type": "tool_selection",
            "tool": tool_names.get(tool_type, "Unknown"),
            "tool_type": tool_type.value
        }
        
        # Execute the appropriate tool
        if tool_type == ToolType.IMAGE_GENERATION:
            yield {"type": "status", "message": "Gerando imagem..."}
            image_url = await self.generate_image(user_message, model=image_model)
            yield {
                "type": "image",
                "url": image_url,
                "prompt": user_message
            }
            
            # Add to conversation history (bounded)
            self._add_to_history_bounded(
                user_message,
                f"Imagem gerada com sucesso! URL: {image_url}"
            )
        
        elif tool_type == ToolType.SEARCH:
            yield {"type": "status", "message": "Pesquisando na web..."}
            full_response = ""
            async for chunk in self.search_web(user_message, model=search_model):
                full_response += chunk
                yield {
                    "type": "text_chunk",
                    "content": chunk
                }
            
            # Add to conversation history (bounded)
            self._add_to_history_bounded(user_message, full_response)
        
        elif tool_type == ToolType.TEXT_TO_SPEECH:
            yield {"type": "status", "message": "Gerando áudio..."}
            audio_url = await self.generate_audio_url(user_message, voice=audio_voice)
            yield {
                "type": "audio",
                "url": audio_url,
                "text": user_message
            }
            
            # Add to conversation history (bounded)
            self._add_to_history_bounded(
                user_message,
                "Áudio gerado com sucesso!"
            )
        
        elif tool_type == ToolType.REASONING:
            yield {"type": "status", "message": "Pensando profundamente..."}
            full_response = ""
            async for chunk in self.generate_text_stream(
                user_message,
                model=reasoning_model,
                system_prompt="Você é um assistente que pensa profundamente sobre problemas complexos."
            ):
                full_response += chunk
                yield {
                    "type": "text_chunk",
                    "content": chunk
                }
            
            # Add to conversation history (bounded)
            self._add_to_history_bounded(user_message, full_response)
        
        else:  # TEXT_GENERATION
            yield {"type": "status", "message": "Gerando resposta..."}
            full_response = ""
            async for chunk in self.generate_text_stream(
                user_message,
                model=text_model,
                system_prompt="Você é um assistente útil e amigável que responde em português."
            ):
                full_response += chunk
                yield {
                    "type": "text_chunk",
                    "content": chunk
                }
            
            # Add to conversation history (bounded)
            self._add_to_history_bounded(user_message, full_response)
        
        # Signal completion
        yield {"type": "done"}
    
    def _add_to_history_bounded(self, user_message: str, assistant_response: str):
        """
        Add messages to history and keep it bounded to prevent unbounded growth
        """
        self.conversation_history.append({"role": "user", "content": user_message})
        self.conversation_history.append({"role": "assistant", "content": assistant_response})
        
        # Keep only last 10 messages (5 exchanges)
        if len(self.conversation_history) > 10:
            self.conversation_history = self.conversation_history[-10:]
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []

"""
Simple tests for the Mega Agent
Run with: pytest test_agent.py
"""
import pytest
import pytest_asyncio
import asyncio
from agent import PollinationsAgent, ToolType


@pytest_asyncio.fixture
async def agent():
    """Create an agent instance for testing"""
    agent = PollinationsAgent()
    yield agent
    await agent.close()


class TestToolDetermination:
    """Test tool selection logic"""
    
    def test_image_generation_keywords(self):
        agent = PollinationsAgent()
        
        # Test various image keywords
        assert agent._determine_tool("crie uma imagem de um gato") == ToolType.IMAGE_GENERATION
        assert agent._determine_tool("desenhe um cachorro") == ToolType.IMAGE_GENERATION
        assert agent._determine_tool("gere uma foto de paisagem") == ToolType.IMAGE_GENERATION
        assert agent._determine_tool("create a picture of sunset") == ToolType.IMAGE_GENERATION
    
    def test_search_keywords(self):
        agent = PollinationsAgent()
        
        # Test search keywords
        assert agent._determine_tool("pesquise sobre IA") == ToolType.SEARCH
        assert agent._determine_tool("busque informações sobre Python") == ToolType.SEARCH
        assert agent._determine_tool("search for latest news") == ToolType.SEARCH
        assert agent._determine_tool("o que está acontecendo no mundo") == ToolType.SEARCH
    
    def test_audio_keywords(self):
        agent = PollinationsAgent()
        
        # Test audio keywords
        assert agent._determine_tool("fale olá") == ToolType.TEXT_TO_SPEECH
        assert agent._determine_tool("diga bom dia") == ToolType.TEXT_TO_SPEECH
        assert agent._determine_tool("speak this text") == ToolType.TEXT_TO_SPEECH
        assert agent._determine_tool("gere áudio dizendo teste") == ToolType.TEXT_TO_SPEECH
    
    def test_reasoning_keywords(self):
        agent = PollinationsAgent()
        
        # Test reasoning keywords
        assert agent._determine_tool("pense sobre isso") == ToolType.REASONING
        assert agent._determine_tool("raciocine sobre o problema") == ToolType.REASONING
        assert agent._determine_tool("think deeply about this") == ToolType.REASONING
        assert agent._determine_tool("analise profundamente") == ToolType.REASONING
    
    def test_default_text_generation(self):
        agent = PollinationsAgent()
        
        # Test default behavior
        assert agent._determine_tool("olá, como vai?") == ToolType.TEXT_GENERATION
        assert agent._determine_tool("explique o que é IA") == ToolType.TEXT_GENERATION
        assert agent._determine_tool("conte-me uma história") == ToolType.TEXT_GENERATION


class TestConversationHistory:
    """Test conversation history management"""
    
    def test_history_starts_empty(self):
        agent = PollinationsAgent()
        assert len(agent.conversation_history) == 0
    
    def test_clear_history(self):
        agent = PollinationsAgent()
        agent.conversation_history = [
            {"role": "user", "content": "test"},
            {"role": "assistant", "content": "response"}
        ]
        agent.clear_history()
        assert len(agent.conversation_history) == 0


@pytest.mark.asyncio
class TestImageGeneration:
    """Test image generation functionality"""
    
    async def test_generate_image_url(self, agent):
        """Test that image generation returns a valid URL"""
        url = await agent.generate_image("a beautiful sunset", model="flux")
        assert url.startswith("https://image.pollinations.ai/")
        assert "sunset" in url.lower() or "beautiful" in url.lower()
    
    async def test_generate_image_with_params(self, agent):
        """Test image generation with custom parameters"""
        url = await agent.generate_image(
            "a cat",
            model="flux",
            width=512,
            height=512,
            seed=42
        )
        assert url.startswith("https://image.pollinations.ai/")


@pytest.mark.asyncio
class TestAudioGeneration:
    """Test audio generation functionality"""
    
    async def test_generate_audio_url(self, agent):
        """Test that audio generation returns a valid URL"""
        url = await agent.generate_audio_url("Hello world", voice="nova")
        assert url.startswith("https://text.pollinations.ai/")
        assert "model=openai-audio" in url
        assert "voice=nova" in url


class TestModelLists:
    """Test that model lists are properly defined"""
    
    def test_text_models_exist(self):
        assert len(PollinationsAgent.TEXT_MODELS) > 0
        assert "openai" in PollinationsAgent.TEXT_MODELS
    
    def test_image_models_exist(self):
        assert len(PollinationsAgent.IMAGE_MODELS) > 0
        assert "flux" in PollinationsAgent.IMAGE_MODELS
    
    def test_audio_voices_exist(self):
        assert len(PollinationsAgent.AUDIO_VOICES) > 0
        assert "nova" in PollinationsAgent.AUDIO_VOICES
    
    def test_search_models_exist(self):
        assert len(PollinationsAgent.SEARCH_MODELS) > 0
        assert "searchgpt" in PollinationsAgent.SEARCH_MODELS
    
    def test_reasoning_models_exist(self):
        assert len(PollinationsAgent.REASONING_MODELS) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

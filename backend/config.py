"""
Configuration settings for the Mega Agent backend
"""
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # API Configuration
    api_title: str = "Mega Agent API"
    api_version: str = "1.0.0"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    # CORS Configuration
    cors_origins: list = ["*"]
    cors_allow_credentials: bool = True
    cors_allow_methods: list = ["*"]
    cors_allow_headers: list = ["*"]
    
    # Pollinations.AI Configuration
    pollinations_text_url: str = "https://text.pollinations.ai"
    pollinations_image_url: str = "https://image.pollinations.ai"
    
    # Request Configuration
    request_timeout: float = 300.0
    max_conversation_history: int = 6  # Last 3 exchanges
    
    # Model Defaults
    default_text_model: str = "openai"
    default_search_model: str = "searchgpt"
    default_reasoning_model: str = "openai-reasoning"
    default_image_model: str = "flux"
    default_audio_voice: str = "nova"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()

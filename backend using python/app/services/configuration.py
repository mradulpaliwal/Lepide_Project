# app/config.py

from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # Basic configurations
    app_name: str = "Document Summarizer"
    upload_dir: str = "uploads/"
    max_file_size: int = 10 * 1024 * 1024  # 10 MB file size limit
    
    # Environment-specific settings
    environment: str = "development"  # Can be "development" or "production"
    debug: bool = True

    # LLM model settings (e.g., model type, paths)
    llm_model: str = "gpt2"  # Model to use for summarization
    
    # Load from .env file (if you have one)
    class Config:
        env_file = ".env"

# Instantiate settings to be used in the app
settings = Settings()

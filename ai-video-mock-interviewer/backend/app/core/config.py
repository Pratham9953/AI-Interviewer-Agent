from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env:str="development"
    port:int=8000
    api_prefix:str="/api"
    database_url:str="postgresql+asyncpg://postgres:postgres@localhost:5432/ai_interviewer"
    sync_database_url:str="postgresql://postgres:postgres@localhost:5432/ai_interviewer"="postgresql+asyncpg://postgres:postgres@localhost:5432/ai_interviewer"
    redis_url:str="redis://localhost:6379/0"
    jwt_secret:str="change_me"
    jwt_algorithm:str="HS256"
    jwt_access_token_expire_minutes:int=1440
    livekit_url:str=""
    livekit_api_key:str=""
    livekit_api_secret:str=""
    openai_api_key:str=""
    openai_model:str="gpt-4o-mini"
    openai_embedding_model:str="text-embedding-3-small"
    ollama_base_url:str="http://localhost:11434"
    ollama_model:str="llama3.1"
    deepgram_api_key:str=""
    deepgram_tts_model:str="aura-2-thalia-en"
    aws_access_key_id:str=""
    aws_secret_access_key:str=""
    aws_region:str="ap-south-1"
    s3_bucket_name:str=""
    cors_origins:str="http://localhost:5173"
    class Config: env_file='.env'
settings=Settings()

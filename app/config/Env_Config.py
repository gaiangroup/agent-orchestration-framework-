import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

ENV = os.getenv("ENVIRONMENT", "development")


if ENV == "production":
    load_dotenv("app/.env.prod")
else:
    load_dotenv("app/.env.dev")


class Env(BaseSettings):
    ENVIRONMENT: str = ENV
    DEBUG: bool
    TF_ENTITY_INGESTION_BASE_URL:str
    AOF_SERVER_V2_URL:str
    AOF_SERVER_V1_URL:str
    GPT_SERVICE_BASE_URL:str


    class Config:
        case_sensitive = True

env = Env()

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    resend_api_key: str
    sender_email: str = "onboarding@resend.dev"
    sender_name: str = "Email Microservice"
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    alpha_vantage_api_key: str
    mongodb_database:str
    mongodb_url:str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

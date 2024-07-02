from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    
    LASTFM_API_KEY: str
    LASTFM_API_SECRET: str
    LASTFM_USERNAME: str
    LASTFM_PASSWORD: str
    OPEN_WEATHER_API_KEY: str
    API_KEY: str
    LOG_LEVEL: str
    OPEN_WEATHER_API_BASE: str


settings = Config()
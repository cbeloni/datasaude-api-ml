from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

_host = os.environ.get('MYSQL_HOST')
_database = os.environ.get('MYSQL_DATABASE')
_user = os.environ.get('MYSQL_USER')
_password = os.environ.get('MYSQL_PASSWORD')

class Settings(BaseSettings):    
    MYSQL_HOST: str = os.environ.get('MYSQL_HOST')
    MYSQL_DATABASE: str = os.environ.get('MYSQL_DATABASE')
    MYSQL_USER: str = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD: str = os.environ.get('MYSQL_PASSWORD')
    WRITER_DB_URL: str = f"mysql+aiomysql://{_user}:{_password}@{_host}:3306/{_database}"
    READER_DB_URL: str = f"mysql+aiomysql://{_user}:{_password}@{_host}:3306/{_database}"

settings = Settings()


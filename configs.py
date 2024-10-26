import os
from typing import List
from pydantic import BaseSettings, Field
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    url_database: str = os.getenv('URL_DATABASE')
    
config = Config()
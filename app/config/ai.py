import json
import os

from pathlib import Path
from sys import path

import loguru

from app.config.app import app_config
from app.config.base import BaseConfig


class AIConfig(BaseConfig):
    _CONFIG_NAME = "ai settings"
    _CONFIG_FILENAME = "ai_config.json"
    AI_API_KEY = ""
    AI_PROVIDER_URL = "https://api.proxyapi.ru/openai/v1"


    def __init__(
            self
    ):
        self.AI_API_KEY = None
        self.AI_PROVIDER_URL = "https://api.proxyapi.ru/openai/v1"

        super().__init__()




ai_config = AIConfig()


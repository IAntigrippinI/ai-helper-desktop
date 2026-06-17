import traceback

import loguru

from langchain_openai import ChatOpenAI

from app.config.ai import ai_config

class OpenAIConnector:

    def __init__(self):
        self.chat = None


    def _get_chat(self):
        if self.chat is None:
            try:
                self.chat = ChatOpenAI(
                    api_key=ai_config.AI_API_KEY,
                    base_url=ai_config.AI_PROVIDER_URL
                )
            except Exception as e:
                loguru.logger.debug(traceback.format_exc())
                loguru.logger.error(f"Error initializing OpenAI: {e}")

        return self.chat


    def get_response(self, prompt: str) -> str:
        chat = self._get_chat()
        response = chat.invoke(prompt)
        loguru.logger.debug(response)
        return response



openai_connector = OpenAIConnector()
import os
from openai import OpenAI

class OpenAIClient:
    def __init__(self, model: str = "gpt-4-1106-preview"):
        self.model = model
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def chat_completion(self, messages, functions=None, function_call="auto"):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            functions=functions,
            function_call=function_call
        )
        return response 
import os
from openai import OpenAI

class ConversationManager:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def send_message(self, messages):
        """
        Send a list of messages to the OpenAI chat completion endpoint and return the assistant's reply.
        messages: List of dicts, e.g. [{"role": "user", "content": "Hello!"}]
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content

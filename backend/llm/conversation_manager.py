import os
from openai import OpenAI

class ConversationManager:
    def __init__(self):
        self.user_histories = {}  # user_id -> list of messages

    def get_history(self, user_id):
        return self.user_histories.get(user_id, [])

    def create_history(self, user_id, initial_messages):
        self.user_histories[user_id] = initial_messages

    def append_message(self, user_id, message):
        if user_id not in self.user_histories:
            self.user_histories[user_id] = []
        self.user_histories[user_id].append(message)

    def set_history(self, user_id, messages):
        self.user_histories[user_id] = messages

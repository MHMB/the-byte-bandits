from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
from data_store.user_data_store import UserDataStore
import os 

SCRIPT_DIR = os.path.dirname(__file__)

class SubmitQuestionnaire(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        username = kwargs.get('username', None)
        user_responses = kwargs.get('user_responses', None)
        if username is None or user_responses is None:
            return None, "Please provide both username and user responses."
        user = UserDataStore().get_user(username)
        user.risk_profile.answers = user_responses
        UserDataStore().update_user(user)

        with open(os.path.join(SCRIPT_DIR, '../evaluation_prompts.md'), 'r') as file:
            eval_prompt = file.read()

        return None, eval_prompt
    
    @classmethod
    def get_name(cls):
        return "submit_questionnaire"
    
    @classmethod
    def get_props(cls):
        return {
            "type": "function",
            "function": {
                "name": "submit_questionnaire",
                "description": "Returns evaluation strategy for the user's responses to the questionnaire",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "required": [
                        "username",
                        "user_responses"
                    ],
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "Username of the user"
                        },
                        "user_responses": {
                            "type": "array",
                            "description": "Array of user responses to the questionnaire in the order they were provided",
                            "items": {
                                "type": "string",
                                "description": "Individual response from the user"
                            }
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
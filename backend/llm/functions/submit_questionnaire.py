from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
from data_store.user_data_store import UserDataStore, RiskProfile
import os 
import logging

SCRIPT_DIR = os.path.dirname(__file__)

class SubmitQuestionnaire(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        logging.warn("SubmitQuestionnaire.run called with args: %s, kwargs: %s", args, kwargs)
        function_args = kwargs.get('function_call_args', None)
        try:
            username = function_args.get('username', None)
            user_responses = function_args.get('user_responses', None)
            if username is None or user_responses is None:
                logging.warning("Missing username or user_responses.")
                return None, "Please provide both username and user responses."
            logging.warn("Fetching user: %s", username)
            user = UserDataStore().get_user(username)
            if user.risk_profile is None:
                user.risk_profile = RiskProfile(
                    risk_score=None,
                    questionnaire_id="12_month",
                    answers=user_responses
                )
            else:
                user.risk_profile.answers = user_responses
            logging.warn("Updating user risk profile answers.")
            UserDataStore().update_user(user)
            with open(os.path.join(SCRIPT_DIR, '../evaluation_prompts.md'), 'r') as file:
                eval_prompt = file.read()
            logging.warn("Evaluation prompt loaded. Length: %d", len(eval_prompt))
            return None, eval_prompt
        except Exception as e:
            logging.exception("Error in SubmitQuestionnaire.run: %s", e)
            return None, f"Error: {e}"
    
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
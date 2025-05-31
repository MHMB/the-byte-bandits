from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
from data_store.user_data_store import UserDataStore
import logging

class StoreEvaluationResult(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        logging.warn("StoreEvaluationResult.run called with args: %s, kwargs: %s", args, kwargs)
        function_args = kwargs.get('function_call_args', None)
        try:
            username = function_args.get('username', None)
            evaluation_result = function_args.get('evaluation_result', None)
            if username is None or evaluation_result is None:
                logging.warning("Missing username or evaluation_result.")
                return None, "Please provide both username and evaluation result."
            logging.warn("Fetching user: %s", username)
            user = UserDataStore().get_user(username)
            user.risk_profile.risk_score = evaluation_result
            logging.warn("Updating user risk profile with evaluation result.")
            UserDataStore().update_user(user)
            return None, "success"
        except Exception as e:
            logging.exception("Error in StoreEvaluationResult.run: %s", e)
            return None, f"Error: {e}"
    
    @classmethod
    def get_name(cls):
        return "store_evaluation_result"
    
    @classmethod
    def get_props(cls):
        return {
            "type": "function",
            "function": {
            "name": "store_evaluation_result",
            "description": "This function stores the evaluation result of the responses submitted by the user. The return value is either 'success' or 'failure'",
            "parameters": {
                "type": "object",
                "required": [
                "username",
                "evaluation_result"
                ],
                "properties": {
                    "username": {
                        "type": "string",
                        "description": "Username of the user"
                    },
                    "evaluation_result": {
                        "type": "string",
                        "description": "Result of evaluation",
                    }
                },
                "additionalProperties": False
            }
            }
        }
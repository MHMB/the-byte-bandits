from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
from data_store.user_data_store import UserDataStore

class StoreEvaluationResult(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        # TODO: Implement the questionnaire evaluation result storage logic
        username = kwargs.get('username', None)
        evaluation_result = kwargs.get('evaluation_result', None)
        if username is None or evaluation_result is None:   
            return None, "Please provide both username and evaluation result."
        user = UserDataStore().get_user(username)
        user.risk_profile.risk_score = evaluation_result
        UserDataStore().update_user(user)
        return None, "success"
    
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
            "strict": True,
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
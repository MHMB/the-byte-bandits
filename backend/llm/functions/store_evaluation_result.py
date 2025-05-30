from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse

class StoreEvaluationResult(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        # TODO: Implement the questionnaire evaluation result storage logic
        function_args = kwargs.get('function_call_args')
        return None, "Summarize the evaluation result and politely inform that the evaluation result has been successfully stored."
    
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
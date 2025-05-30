from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse

class GenerateQuiz(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        # TODO: Implement the quiz generation logic
        function_args = kwargs.get('function_call_args')
        return None, "Generate a quiz for the user to answer."
    
    @classmethod
    def get_name(cls):
        return "get_user_questionnaire"
    
    @classmethod
    def get_props(cls):
        return {
            "type": "function",
            "function": {
                "name": "get_user_questionnaire",
                "description": "Presents a short quiz based on the user's investment horizon for portfolio creation",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "required": [
                    "horizon"
                    ],
                    "properties": {
                        "horizon": {
                            "type": "string",
                            "description": "Investment horizon for the user's portfolio, which can be one of: '6_month', '12_month', '1_3_years', '3_10_years', '10_plus_years'.",
                            "enum": [
                            "6_month",
                            "12_month",
                            "1_3_years",
                            "3_10_years",
                            "10_plus_years"
                            ]
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
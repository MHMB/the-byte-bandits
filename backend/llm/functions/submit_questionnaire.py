from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse

class SubmitQuestionnaire(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        # TODO: Implement the questionnaire submission logic. This function returns evaluation strategy for the user's responses to the questionnaire. (Tof kon birun kamel)
        function_args = kwargs.get('function_call_args')
        return None, "Summarize the questionnaire and politely inform that the questionnaire has been successfully submitted."
    
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
                    "user_responses"
                    ],
                    "properties": {
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
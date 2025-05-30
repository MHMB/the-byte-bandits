from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse

class StoreUserInfo(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        function_args = kwargs.get('function_call_args')
        return None, "Summarize the order and politely inform that the order has been successfully created."
    
    @classmethod
    def get_name(cls):
        return ""
    
    @classmethod
    def get_props(cls, store_profile: Optional[dict] = None):
        return {
            "type": "function",
            "function": {
                "name": "store_investment_parameters",
                "description": "Stores investment parameters in the database and returns the user ID or -1 if unsuccessful.",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "required": [
                    "age",
                    "investment_amount",
                    "increase_rate"
                    ],
                    "properties": {
                        "age": {
                            "type": "number",
                            "description": "The age of the user (nullable)"
                        },
                        "investment_amount": {
                            "type": "number",
                            "description": "The total amount of money invested (nullable)"
                        },
                        "increase_rate": {
                            "type": "number",
                            "description": "The expected rate of increase on the investment (nullable)"
                        },
                        "investment_horizon_duration": {
                            "type": "number",
                            "description": "The duration of the investment horizon"
                        },
                        "investment_horizon_unit": {
                            "type": "string",
                            "description": "The unit of the investment horizon",
                            "enum": ["year", "month", "day", "week"]
                        }
                    },
                    "additionalProperties": False
                }
            }
        }   
    
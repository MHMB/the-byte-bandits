from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse

class StoreUserPortfolio(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        function_args = kwargs.get('function_call_args')
        return None, "Summarize the order and politely inform that the order has been successfully created."
    
    @classmethod
    def get_name(cls):
        return "store_user_portfolio"
    
    @classmethod
    def get_props(cls, store_profile: Optional[dict] = None):
        return {
            "type": "function",
            "function": {
                "name": "store_user_portfolio",
                "description": "Store the suggested portfolio to the user profile by giving the username. It must provide each asset (gold, crypto, real-estate, USD, stock) name and percentage of the total portfolio.",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "required": [
                    "username",
                    "portfolio"
                    ],
                    "properties": {
                    "username": {
                        "type": "string",
                        "description": "The username of the user to whom the portfolio is associated"
                    },
                    "portfolio": {
                        "type": "array",
                        "description": "Array of assets in the portfolio, including their names and percentages",
                        "items": {
                        "type": "object",
                        "required": [
                            "asset_name",
                            "percentage"
                        ],
                        "properties": {
                            "asset_name": {
                            "type": "string",
                            "description": "The name of the asset (e.g., gold, crypto, real-estate, USD, stock)"
                            },
                            "percentage": {
                            "type": "number",
                            "description": "The percentage of the total portfolio that this asset represents"
                            }
                        },
                        "additionalProperties": False
                        }
                    }
                    },
                    "additionalProperties": False
                }
            }
        }   
    
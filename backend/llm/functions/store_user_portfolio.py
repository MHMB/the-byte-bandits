from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
from data_store.user_data_store import UserDataStore
from models.portfolio import Portfolio

class StoreUserPortfolio(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        username = kwargs.get('username', None)
        portfolio_data = kwargs.get('portfolio', None)
        if username is None or portfolio_data is None:
            return None, "Please provide both username and portfolio data."
        
        portfolio = Portfolio(assets=portfolio_data)
        user = UserDataStore().get_user(username)
        if user is None:
            return None, f"User with username '{username}' does not exist."
        user.portfolio = portfolio
        UserDataStore().update_user(user)
        return None, "success"
    
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
    
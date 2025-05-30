from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
from models.user import UserProfile
from data_store.user_data_store import UserDataStore

class StoreInvestmentParameters(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        age = kwargs.get('age', None)
        investment_amount = kwargs.get('investment_amount', None)
        increase_rate = kwargs.get('increase_rate', None)
        investment_horizon_duration = kwargs.get('investment_horizon_duration', None)
        investment_horizon_unit = kwargs.get('investment_horizon_unit', None)
        if age is None or investment_amount is None or increase_rate is None or investment_horizon_duration is None or investment_horizon_unit is None:
            return None, "Please provide all required parameters: age, investment_amount, increase_rate, investment_horizon_duration, and investment_horizon_unit."
        
        user_profile = UserProfile(
            username="1",
            age=age,
            initial_investment=investment_amount,
            investment_increase_rate=increase_rate,
            investment_horizon={
                "duration": investment_horizon_duration,
                "unit": investment_horizon_unit
            }
        )
        # Store the user profile in the data store
        user_data_store = UserDataStore()
        user_data_store.create_user(user_profile)
        # create user and return the username
        return None, "1"
    
    @classmethod
    def get_name(cls):
        return "store_investment_parameters"
    
    @classmethod
    def get_props(cls):
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
    
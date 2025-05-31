from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
from models.user import UserProfile
from data_store.user_data_store import UserDataStore
import logging
from traceback import format_exc

class StoreInvestmentParameters(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        function_args = kwargs.get('function_call_args', None)
        logging.warning("StoreInvestmentParameters.run called with args: %s, kwargs: %s", args, kwargs)
        try:
            age = function_args.get('age', None)
            investment_amount = function_args.get('investment_amount', None)
            increase_rate = function_args.get('increase_rate', None)
            investment_horizon_duration = function_args.get('investment_horizon_duration', None)
            investment_horizon_unit = function_args.get('investment_horizon_unit', None)
            if age is None or investment_amount is None or increase_rate is None or investment_horizon_duration is None or investment_horizon_unit is None:
                logging.warning("Missing one or more required parameters.")
                return None, "Please provide all required parameters: age, investment_amount, increase_rate, investment_horizon_duration, and investment_horizon_unit."
            logging.warn("Creating UserProfile object.")
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
            user_data_store = UserDataStore()
            logging.warn("Storing user profile in data store.")
            user_data_store.add_user(user_profile)
            logging.warn("User profile created successfully.")
            return None, "User profile created and updated successfully. The username of the user is 1"
        except Exception as e:
            logging.exception("Error in StoreInvestmentParameters.run: %s", format_exc())
            return None, f"Error: {e}"
    
    @classmethod
    def get_name(cls):
        return "store_investment_parameters"
    
    @classmethod
    def get_props(cls):
        return {
            "type": "function",
            "function": {
                "name": "store_investment_parameters",
                "description": "Stores investment parameters in the database and returns the username of the user",
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
    
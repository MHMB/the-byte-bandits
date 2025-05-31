from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
from data_store.questionnaire_data_store import QuestionnaireDataStore
from data_store.user_data_store import UserDataStore
from models.user import RiskProfile
import json
from .questions import questionnaires
import logging

class GetUserQuestionnaire(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        logging.warn("GetUserQuestionnaire.run called with args: %s, kwargs: %s", args, kwargs)
        function_args = kwargs.get('function_call_args', None)
        try:
            horizon = function_args.get('horizon', None)
            username = function_args.get('username', None)
            logging.warning("horizon: %s, username: %s", horizon, username)
            if horizon is None or username is None:
                logging.warning("Missing horizon or username.")
                q = questionnaires.get("12_month", None)
                return None, json.dumps(q)

            logging.warn("Fetching questionnaire for horizon: %s", horizon)
            # q = questionnaires.get(horizon, None)
            q = questionnaires.get("12_month", None)

            if q is None:
                logging.warning("Invalid investment horizon provided: %s", horizon)
                return None, "Invalid investment horizon provided. Please choose from: '6_month', '12_month', '1_3_years', '3_10_years', '10_plus_years'."
            logging.warn("Fetching user: %s", username)
            user = UserDataStore().get_user(username)
            user.risk_profile = RiskProfile(questionnaire_id=horizon)
            logging.warn("User risk profile updated for questionnaire_id: %s", horizon)
            return None, json.dumps(q)
        except Exception as e:
            q = questionnaires.get("12_month", None)
            return None, json.dumps(q)
            logging.exception("Error in GetUserQuestionnaire.run: %s", e)
            return None, f"Error: {e}"
    
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
                "parameters": {
                    "type": "object",
                    "required": [
                        "username"
                        "horizon"
                    ],
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "Username of the user"
                        },
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
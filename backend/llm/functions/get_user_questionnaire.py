from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
from data_store.questionnaire_data_store import QuestionnaireDataStore
from data_store.user_data_store import UserDataStore
from models.user import RiskProfile
import json
from .questions import questionnaires

class GetUserQuestionnaire(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        horizon = kwargs.get('horizon', None)
        username = kwargs.get('username', None)
        if horizon is None or username is None:
            return None, "Please provide both username and investment horizon."
        # q = QuestionnaireDataStore().get_questionnaire(horizon)       # not now, we're in rush!!
        q = questionnaires.get(horizon, None)
        if q is None:
            return None, "Invalid investment horizon provided. Please choose from: '6_month', '12_month', '1_3_years', '3_10_years', '10_plus_years'."
        user = UserDataStore().get_user(username)
        user.risk_profile = RiskProfile(questionnaire_id=horizon)
        return None, json.dumps(q)
    
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
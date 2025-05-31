from pydantic import BaseModel
from typing import Optional, List, Literal
from .portfolio import Portfolio

class InvestmentHorizon(BaseModel):
    duration: int
    unit: str

class RiskProfile(BaseModel):
    risk_score: Optional[dict]
    answers: Optional[List[int]] = None         # answer index (0, 1, 2, 3 for multiple choice)
    questionnaire_id: str # "6_month", "12_month", "1_3_years", "3_10_years", "10_plus_years"

class UserProfile(BaseModel):
    username: str
    risk_profile: Optional[RiskProfile] = None
    portfolio: Optional[Portfolio] = None
    chat_id: Optional[str] = None
    initial_investment: Optional[float] = None
    investment_horizon: Optional[InvestmentHorizon] = None
    investment_increase_rate: Optional[float] = None
    
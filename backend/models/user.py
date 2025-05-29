from pydantic import BaseModel
from typing import Optional, List
from .portfolio import Portfolio

class InvestmentHorizon(BaseModel):
    duration: int
    unit: str

class RiskProfile(BaseModel):
    risk_score: dict
    answers: Optional[List[int]] = None         # answer index (0, 1, 2, 3 for multiple choice)
    questions: Optional[List[str]] = None       # question ids

class UserProfile(BaseModel):
    username: str
    risk_profile: Optional[RiskProfile] = None
    portfolio: Optional[Portfolio] = None
    chat_id: Optional[str] = None
    initial_investment: Optional[float] = None
    investment_horizon: Optional[InvestmentHorizon] = None
    
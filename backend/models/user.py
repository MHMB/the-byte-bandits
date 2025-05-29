from pydantic import BaseModel
from typing import Optional, List


class InvestmentHorizon(BaseModel):
    duration: int
    unit: str

class RiskProfile(BaseModel):
    risk_score: int
    answers: Optional[list] = None

class UserProfile(BaseModel):
    username: str
    risk_profile: Optional[RiskProfile] = None
    portfolio: Optional[list] = None 
    chat_id: Optional[str] = None
    initial_investment: Optional[float] = None
    investment_horizon: Optional[InvestmentHorizon] = None
    
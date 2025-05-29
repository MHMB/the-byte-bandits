from pydantic import BaseModel
from typing import Optional, List

class RiskProfile(BaseModel):
    risk_score: int
    answers: Optional[list] = None

class UserProfile(BaseModel):
    username: str
    risk_profile: Optional[RiskProfile] = None
    portfolio: Optional[list] = None 
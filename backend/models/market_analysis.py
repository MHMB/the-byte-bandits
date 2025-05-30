from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MarketAnalysis(BaseModel):
    asset_class: str
    analysis: str
    date: Optional[datetime] = None
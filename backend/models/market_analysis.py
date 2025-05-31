from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class MarketAnalysis(BaseModel):
    asset_class: Literal['stocks', 'gold', 'usd', 'crypto', 'real_estate']
    analysis: str
    date: Optional[datetime] = datetime.now()
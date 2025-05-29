from pydantic import BaseModel
from typing import List, Optional

class AssetReport(BaseModel):
    asset_class: str
    report: str

class PortfolioAsset(BaseModel):
    asset_class: str
    allocation: float
    report: Optional[AssetReport] = None

class Portfolio(BaseModel):
    assets: List[PortfolioAsset] 
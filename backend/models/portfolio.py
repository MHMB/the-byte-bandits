from pydantic import BaseModel
from typing import List, Optional

class AssetBase(BaseModel):
    asset_class: str
    allocation: float
    report: Optional[str] = None
    place: Optional[str] = None             # Nobitex, etc.
    symbol: Optional[str] = None            # USDT - Bource Namad
    buying_price: Optional[float] = None
    selling_price: Optional[float] = None

class GoldAsset(AssetBase):
    asset_class: str = "Gold"
    
class USDAsset(AssetBase):
    asset_class: str = "USD"

class StockAsset(AssetBase):
    asset_class: str = "Stock"

class Portfolio(BaseModel):
    assets: List[AssetBase] = []
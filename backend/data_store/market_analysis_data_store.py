from db.mongo import MongoDB
from models.market_analysis import MarketAnalysis

class MarketAnalysisDataStore:
    def __init__(self):
        self.collection = MongoDB().get_collection("market_analyses")

    def add_analysis(self, asset_class: str, analysis: MarketAnalysis):
        self.collection.update_one(
            {"asset_class": asset_class},
            {"$set": analysis.model_dump()},
            upsert=True
        )

    def get_analysis(self, asset_class: str) -> MarketAnalysis:
        data = self.collection.find_one({"asset_class": asset_class})
        if data:
            return MarketAnalysis(**data)
        return None

    def update_analysis(self, asset_class: str, analysis: MarketAnalysis):
        self.collection.update_one({"asset_class": asset_class}, {"$set": analysis.model_dump()})

    def delete_analysis(self, asset_class: str):
        self.collection.delete_one({"asset_class": asset_class})
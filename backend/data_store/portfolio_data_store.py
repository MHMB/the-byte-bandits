from db.mongo import MongoDB
from models.portfolio import Portfolio

class PortfolioDataStore:
    def __init__(self):
        self.collection = MongoDB().get_collection("portfolios")

    def add_portfolio(self, username: str, portfolio: Portfolio):
        self.collection.update_one(
            {"username": username},
            {"$set": portfolio.model_dump()},
            upsert=True
        )

    def get_portfolio(self, username: str) -> Portfolio:
        data = self.collection.find_one({"username": username})
        if data:
            return Portfolio(**data)
        return None

    def update_portfolio(self, username: str, portfolio: Portfolio):
        self.collection.update_one({"username": username}, {"$set": portfolio.model_dump()})

    def delete_portfolio(self, username: str):
        self.collection.delete_one({"username": username})
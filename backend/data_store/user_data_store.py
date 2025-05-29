from db.mongo import MongoDB
from models.user import UserProfile, InvestmentHorizon, RiskProfile

class UserDataStore:
    def __init__(self):
        self.collection = MongoDB().get_collection("users")

    def add_user(self, user: UserProfile):
        self.collection.update_one(
            {"username": user.username},
            {"$set": user.model_dump()},
            upsert=True
        )

    def get_user(self, username: str) -> UserProfile:
        data = self.collection.find_one({"username": username})
        if data:
            return UserProfile(**data)
        return None

    def update_user(self, username: str, user: UserProfile):
        self.collection.update_one({"username": username}, {"$set": user.model_dump()})

    def delete_user(self, username: str):
        self.collection.delete_one({"username": username})

    def add_portfolio(self, username: str, portfolio):
        user = self.get_user(username)
        if user:
            user.portfolio = portfolio
            self.update_user(username, user)

if __name__ == "__main__":
    from db.mongo import MongoDB
    from models.portfolio import Portfolio, AssetBase, GoldAsset, USDAsset, StockAsset

    MongoDB('mongodb://localhost:27018/roboadvisor')
    
    # Example usage - Creating User
    user_store = UserDataStore()
    new_user = UserProfile(username="test_user")
    new_user.investment_horizon = InvestmentHorizon(duration=5, unit="years")
    new_user.risk_profile = RiskProfile(
        risk_score={"score": 5, "description": "Moderate"},
        questions=["Q1", "Q2", "Q3", "Q4"],
        answers=[0, 2, 1, 1])
    new_user.initial_investment = 10000.0
    user_store.add_user(new_user)
    retrieved_user = user_store.get_user("test_user")

    # Example usage - Adding Portfolio
    portfolio = Portfolio(assets=[
        GoldAsset(asset_class="Gold", allocation=0.4, buying_price=1800.0),
        USDAsset(asset_class="USD", allocation=0.3, buying_price=1.0),
        StockAsset(asset_class="Stock", allocation=0.3, buying_price=150.0)
    ])
    user_store.add_portfolio("test_user", portfolio)
    # Retrieve and print the user
    retrieved_user = user_store.get_user("test_user")

    print(retrieved_user)
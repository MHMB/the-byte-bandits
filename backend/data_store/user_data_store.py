from db.mongo import MongoDB
from models.user import UserProfile, InvestmentHorizon, RiskProfile
from .questionnaire_data_store import QuestionnaireDataStore

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

    def get_user_questionnaire_answers(self, username: str) -> list:
        """
        Returns a list of dicts: [{"q": question_text, "a": answer_text}, ...]
        for the given user's questionnaire and their answers.
        `questionnaire_lookup_func` should accept a questionnaire_id and return a Questionnaire object.
        """
        user = self.get_user(username)
        if not user or not user.risk_profile or not user.risk_profile.answers:
            return []

        questionnaire_id = user.risk_profile.questionnaire_id
        answers = user.risk_profile.answers
        questionnaire = QuestionnaireDataStore().get_questionnaire(questionnaire_id)
        if not questionnaire:
            return []

        result = []
        for idx, question in enumerate(questionnaire.questions):
            answer_idx = answers[idx] if idx < len(answers) else None
            answer_text = question.options[answer_idx] if answer_idx is not None and answer_idx < len(question.options) else None
            result.append({"q": question.text, "a": answer_text})
        return result

if __name__ == "__main__":
    from db.mongo import MongoDB
    from models.portfolio import Portfolio, GoldAsset, USDAsset, StockAsset

    MongoDB('mongodb://localhost:27018/roboadvisor')
    
    # Example usage - Creating User
    user_store = UserDataStore()
    new_user = UserProfile(username="test_user")
    new_user.investment_horizon = InvestmentHorizon(duration=5, unit="years")
    new_user.risk_profile = RiskProfile(
        risk_score={"score": 5, "description": "Moderate"},
        questionnaire_id="6_month",
        answers=[0, 2])
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
    print(user_store.get_user_questionnaire_answers("test_user"))

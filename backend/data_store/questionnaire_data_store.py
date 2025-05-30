from db.mongo import MongoDB
from models.questionnaire import Questionnaire

class QuestionnaireDataStore:
    def __init__(self):
        self.collection = MongoDB().get_collection("questionnaires")

    def upsert_questionnaire(self, questionnaire: Questionnaire):
        self.collection.update_one(
            {"id": questionnaire.id},
            {"$set": questionnaire.model_dump()},
            upsert=True
        )

    def get_questionnaire(self, questionnaire_id: str) -> Questionnaire:
        data = self.collection.find_one({"id": questionnaire_id})
        if data:
            return Questionnaire(**data)
        return None

    def delete_questionnaire(self, questionnaire_id: str):
        self.collection.delete_one({"id": questionnaire_id})

    def get_all_questionnaires(self):
        return [Questionnaire(**doc) for doc in self.collection.find()]

# Example usage
if __name__ == "__main__":
    from db.mongo import MongoDB
    
    MongoDB('mongodb://localhost:27018/roboadvisor')
    store = QuestionnaireDataStore()
    store.upsert_questionnaire(Questionnaire(
        id="6_month",
        questions=[
            {"text": "In 6 months, what is your investment goal?", "options": ["Growth", "Income", "Preservation"]},
            {"text": "In 6 months, what is your risk tolerance?", "options": ["Low", "Medium", "High"]}
        ]
    ))
    store.upsert_questionnaire(Questionnaire(
        id="12_month",
        questions=[
            {"text": "In 12 months, what is your investment goal?", "options": ["Growth", "Income", "Preservation"]},
            {"text": "In 12 months, what is your risk tolerance?", "options": ["Low", "Medium", "High"]}
        ]
    ))
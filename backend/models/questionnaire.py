from pydantic import BaseModel
from typing import Optional, List, Union, Literal
from .portfolio import Portfolio

class Question(BaseModel):
    text: str
    options: List[str]

class Questionnaire(BaseModel):
    id: Literal["6_month", "12_month", "1_3_years", "3_10_years", "10_plus_years"]
    questions: List[Question]
    
from typing import Type, Dict

from .function_interface import Function
from .get_usd_market_data import GetUSDMarketData
from .get_gold_market_data import GetGoldMarketData
from .get_real_estate_market_data import GetRealEstateMarketData
from .get_user_questionnaire import GetUserQuestionnaire
from .submit_questionnaire import SubmitQuestionnaire
from .store_evaluation_result import StoreEvaluationResult
from .store_user_portfolio import StoreUserPortfolio
from .get_user_questionnaire import GetUserQuestionnaire

class FunctionFactory:
    _registry: Dict[str, Type[Function]] = {}

    @classmethod
    def register_function(cls, function: Type[Function]):
        cls._registry[function.get_name()] = function

    @classmethod
    def get_function(cls, name: str) -> Type[Function]:
        if name not in cls._registry:
            raise ValueError(f"Function {name} not found")
        return cls._registry[name]

FunctionFactory.register_function(GetUSDMarketData) 
FunctionFactory.register_function(GetGoldMarketData) 
FunctionFactory.register_function(GetRealEstateMarketData)
FunctionFactory.register_function(GetUserQuestionnaire)
FunctionFactory.register_function(SubmitQuestionnaire)
FunctionFactory.register_function(StoreEvaluationResult)
FunctionFactory.register_function(StoreUserPortfolio)
FunctionFactory.register_function(GetUserQuestionnaire)
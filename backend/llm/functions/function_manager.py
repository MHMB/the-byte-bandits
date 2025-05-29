from typing import Type, Dict

from .function_interface import Function
from .get_usd_market_data import GetUSDMarketData
from .get_gold_market_data import GetGoldMarketData
from .get_real_estate_market_data import GetRealEstateMarketData

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
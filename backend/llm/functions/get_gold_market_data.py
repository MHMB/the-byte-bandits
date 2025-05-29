from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
import requests
import json
import datetime as dt

class GetGoldMarketData(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        headers = {
            'symbol': 'PAXGIRT',
            'resolution': 'D',
            'from': int((dt.datetime.now() - dt.timedelta(days=30)).timestamp()),
            'to': int(dt.datetime.now().timestamp())
        }
        gold_data = requests.get('https://api.nobitex.ir/market/udf/history', headers=headers).json()
        return None, json.dumps(gold_data)
    
    @classmethod
    def get_name(cls):
        return "submit_order"
    
    @classmethod
    def get_props(cls):
        return {
            "type": "function",
            "function": {
                "name": "get_gold_market_data",
                "description": "This function takes no argument and returns the gold market data in JSON format.",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False
                }
            }
        }

        
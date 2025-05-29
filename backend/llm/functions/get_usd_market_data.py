from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
import requests
import datetime as dt
import json

class GetUSDMarkertData(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        headers = {
            'symbol': 'USDTIRT',
            'resolution': 'D',
            'from': int((dt.datetime.now() - dt.timedelta(days=30)).timestamp()),
            'to': int(dt.datetime.now().timestamp())
        }
        usd_data = requests.get('https://api.nobitex.ir/market/udf/history', headers=headers).json()
        return None, json.dumps(usd_data)
    
    @classmethod
    def get_name(cls):
        return "get_usd_market_data"
    
    @classmethod
    def get_props(cls):
        return {
            "type": "function",
            "function": {
                "name": "get_usd_market_data",
                "description": "This function takes no arguments and returns the USD price in Iranian toman as market data in JSON format.",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False
                }
            }
        }
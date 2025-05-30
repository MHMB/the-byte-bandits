from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse


class CreateOrderOrder(Function):
    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        return None, "Summarize the order and politely inform that the order has been successfully created."
    
    @classmethod
    def get_name(cls):
        return "submit_order"
    
    @classmethod
    def get_props(cls, store_profile: Optional[dict] = None):
        return {}
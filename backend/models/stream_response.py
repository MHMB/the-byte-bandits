from typing import List
from pydantic import BaseModel


class StreamResponse(BaseModel):
    status: str = 'success'

class ThreadId(StreamResponse):
    thread_id: str

class TextResponse(StreamResponse):
    text: str

class WaitStatusResponse(StreamResponse):
    wait: bool = True

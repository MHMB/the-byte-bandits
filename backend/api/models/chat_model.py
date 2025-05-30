from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    username: Optional[str]
    message: str

class ChatResponse(BaseModel):
    response_message: str

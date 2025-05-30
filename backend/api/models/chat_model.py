from typing import Optional
from pydantic import BaseModel

class ChatRequest(BaseModel):
    username: Optional[str] = "1"
    message: str

class ChatResponse(BaseModel):
    response_message: str

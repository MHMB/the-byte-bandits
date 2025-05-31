from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    username: Optional[str] = "1"
    message: str

class ChatResponse(BaseModel):
    response_message: str

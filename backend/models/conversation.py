from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

class Message(BaseModel):
    id: str
    role: Literal["user", "assistant", "system"]
    content: str
    timestamp: datetime
    tool_calls: Optional[List[dict]] = None  # For OpenAI function/tool calls

class Conversation(BaseModel):
    id: str
    user_id: str
    messages: List[Message] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime

class User(BaseModel):
    id: str
    name: Optional[str] = None

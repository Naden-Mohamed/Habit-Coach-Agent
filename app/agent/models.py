# models.py
from pydantic import BaseModel
from typing import Optional

class WhatsAppMessage(BaseModel):
    from_number: str
    text: str
    timestamp: Optional[int] = None

class ToolCall(BaseModel):
    tool: str
    params: dict

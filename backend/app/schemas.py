from pydantic import BaseModel, Field


class SupportChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    session_id: str = Field(default="default", min_length=1, max_length=100)


class SupportChatResponse(BaseModel):
    response: str
    session_id: str
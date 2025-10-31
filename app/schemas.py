from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str


class PostResponse(BaseModel):
    id: int
    created_at: str
    title: str
    content: str

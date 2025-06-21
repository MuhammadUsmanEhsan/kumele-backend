from pydantic import BaseModel

class Guideline(BaseModel):
    id: int
    title: str
    description: str

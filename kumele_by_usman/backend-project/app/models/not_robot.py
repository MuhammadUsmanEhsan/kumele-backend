from pydantic import BaseModel

class RobotCheckRequest(BaseModel):
    username: str
    is_human: bool

from pydantic import BaseModel

class FollowRequest(BaseModel):
    follower: str
    following: str

class UsernameRequest(BaseModel):
    username: str

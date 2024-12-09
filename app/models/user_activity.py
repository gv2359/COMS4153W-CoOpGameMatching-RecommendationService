from pydantic import BaseModel


class UserActivity(BaseModel):
    userId: str
    gameId: str
    isMatched: bool
    isInterested: bool

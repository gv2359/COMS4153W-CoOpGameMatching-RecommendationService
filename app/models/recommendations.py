from __future__ import annotations

from typing import List
from app.models.game import Game
from pydantic import BaseModel


class Recommendations(BaseModel):
    userId: str
    games: List[Game]

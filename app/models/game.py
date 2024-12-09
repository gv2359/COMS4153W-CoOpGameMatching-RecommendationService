from typing import Optional, Dict, List
from pydantic import BaseModel

class Game(BaseModel):
    gameId: str
    title: str
    description: Optional[str] = None
    image: Optional[str] = None
    genre: Optional[str] = None
    links: Optional[Dict[str, Dict[str, str]]]

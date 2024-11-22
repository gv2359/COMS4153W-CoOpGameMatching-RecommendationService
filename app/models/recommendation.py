from __future__ import annotations

from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class Recommendation(BaseModel):
    recId: Optional[int] = None
    userId: Optional[str] = None
    gameIDs: Optional[List[str]] = None

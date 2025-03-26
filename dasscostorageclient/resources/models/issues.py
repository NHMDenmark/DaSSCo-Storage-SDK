from pydantic import BaseModel
from datetime import datetime

class IssueModel(BaseModel):
    category: str
    name: str | None
    timestamp: datetime = None
    description: str | None
    note: str | None
    solved: bool

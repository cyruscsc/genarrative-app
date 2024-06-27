from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class DBBase(BaseModel):
    id: UUID


class DBTimestamps(BaseModel):
    created_at: datetime
    updated_at: datetime

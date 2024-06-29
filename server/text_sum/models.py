from pydantic import BaseModel
from utils.models import DBBase, DBTimestamps
from uuid import UUID


class TextSumInput(BaseModel):
    content: str


class TextSumCompletion(BaseModel):
    summary: str


class TextSumToDB(TextSumInput, TextSumCompletion):
    created_by: UUID


class TextSum(DBBase, DBTimestamps, TextSumToDB):
    pass

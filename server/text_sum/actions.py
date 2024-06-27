import asyncio
from fastapi.encoders import jsonable_encoder
from text_sum.models import TextSum, TextSumCompletion, TextSumInput, TextSumToDB
from utils.supabase import supa
from uuid import UUID


async def get_text_sum_from_llm(text: TextSumInput) -> TextSumCompletion:
    await asyncio.sleep(5)
    return TextSumCompletion(
        title="Yay!",
        summary="You got the summary.",
    )


def create_text_sum_to_db(text_sum: TextSumToDB) -> TextSum:
    jsonable_text_sum = jsonable_encoder(text_sum)
    db_text_sum = (
        supa.from_("text_sums")
        .insert(jsonable_text_sum)
        .execute()
        .data[0]
    )
    return TextSum(**db_text_sum)


def get_text_sums_from_db(user_id: UUID) -> list[TextSum]:
    db_text_sums = (
        supa.from_("text_sums")
        .select("*")
        .eq("created_by", str(user_id))
        .execute()
        .data
    )
    return [TextSum(**db_text_sum) for db_text_sum in db_text_sums]


def get_text_sum_from_db(id: UUID) -> TextSum:
    db_text_sum = (
        supa.from_("text_sums")
        .select("*")
        .eq("id", str(id))
        .execute()
        .data[0]
    )
    return TextSum(**db_text_sum)

from fastapi import FastAPI
from fastapi import Depends, HTTPException, Response
from text_sum.actions import (
    create_text_sum_to_db,
    get_text_sum_from_db,
    get_text_sums_from_db,
    get_text_sum_from_llm,
)
from text_sum.models import TextSum, TextSumInput, TextSumToDB
from user.deps import verify_session
from user.models import UserSession

app = FastAPI()


@app.get("/", response_model=list[TextSum])
async def text_sum_get_all_by_user(
    session: UserSession = Depends(verify_session),
) -> list[TextSum]:
    try:
        return get_text_sums_from_db(session.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/{id}", response_model=TextSum)
async def text_sum_get_by_id(
    id: str,
    session: UserSession = Depends(verify_session),
) -> TextSum:
    try:
        db_text_sum = get_text_sum_from_db(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if db_text_sum.created_by != session.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    return db_text_sum


@app.post("/", response_model=TextSum)
async def text_sum_create(
    text: TextSumInput, session: UserSession = Depends(verify_session)
) -> TextSum:
    try:
        llm_text_sum = await get_text_sum_from_llm(text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    try:
        return create_text_sum_to_db(
            TextSumToDB(
                **text.model_dump(),
                **llm_text_sum.model_dump(),
                created_by=session.id,
            )
        )
    except Exception as e:
        raise HTTPException(status_code=499, detail=str(e))

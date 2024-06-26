from fastapi import APIRouter, Depends, HTTPException, Response
from user.actions import sign_up, sign_in, sign_out
from user.cookies import set_tokens, delete_tokens
from user.deps import verify_session
from user.models import User, UserAuth, UserSession, UserTokens

router = APIRouter()


@router.post("/sign-up", response_model=User)
async def user_sign_up(credentials: UserAuth, response: Response) -> User:
    try:
        session = sign_up(credentials)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    set_tokens(
        response,
        UserTokens(
            access_token=session.access_token,
            refresh_token=session.refresh_token,
        ),
    )
    return User(id=session.id, email=session.email)


@router.post("/sign-in", response_model=User)
async def user_sign_in(credentials: UserAuth, response: Response) -> User:
    try:
        session = sign_in(credentials)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    set_tokens(
        response,
        UserTokens(
            access_token=session.access_token,
            refresh_token=session.refresh_token,
        ),
    )
    return User(id=session.id, email=session.email)


@router.post("/sign-out")
async def user_sign_out(
    response: Response, session: UserSession = Depends(verify_session)
) -> None:
    try:
        sign_out(UserTokens(access_token=session.access_token))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    delete_tokens(response)
    return None

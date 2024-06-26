from fastapi import Request, HTTPException
from user.actions import set_session
from user.cookies import get_tokens
from user.models import UserSession


def verify_session(request: Request) -> UserSession:
    tokens = get_tokens(request)
    if not tokens.access_token or not tokens.refresh_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        session = set_session(tokens)
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return session

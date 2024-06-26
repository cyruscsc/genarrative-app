from fastapi import Request, Response
from user.models import UserTokens


def get_tokens(request: Request) -> UserTokens:
    return UserTokens(
        access_token=request.cookies.get("access_token"),
        refresh_token=request.cookies.get("refresh_token"),
    )


def set_tokens(response: Response, tokens: UserTokens) -> Response:
    response.set_cookie("access_token", tokens.access_token)
    response.set_cookie("refresh_token", tokens.refresh_token)
    return response


def delete_tokens(response: Response) -> Response:
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response

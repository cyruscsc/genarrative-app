from user.models import UserAuth, UserSession, UserTokens
from utils.supabase import supa


def sign_up(credentials: UserAuth) -> UserSession:
    auth_response = supa.auth.sign_up(
        {
            "email": credentials.email,
            "password": credentials.password,
        }
    )
    return UserSession(
        id=auth_response.user.id,
        email=auth_response.user.email,
        access_token=auth_response.session.access_token,
        refresh_token=auth_response.session.refresh_token,
    )


def sign_in(credentials: UserAuth) -> UserSession:
    auth_response = supa.auth.sign_in_with_password(
        {
            "email": credentials.email,
            "password": credentials.password,
        }
    )
    return UserSession(
        id=auth_response.user.id,
        email=auth_response.user.email,
        access_token=auth_response.session.access_token,
        refresh_token=auth_response.session.refresh_token,
    )


def sign_out(tokens: UserTokens) -> None:
    return supa.auth.admin.sign_out(tokens.access_token)


def set_session(tokens: UserTokens) -> UserSession:
    auth_response = supa.auth.set_session(
        tokens.access_token,
        tokens.refresh_token,
    )
    return UserSession(
        id=auth_response.user.id,
        email=auth_response.user.email,
        access_token=auth_response.session.access_token,
        refresh_token=auth_response.session.refresh_token,
    )

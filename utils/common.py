import json
from typing import TYPE_CHECKING, Union

from django.http.response import HttpResponse
from jose import jwt

from ecode import OK, E
from ZRT.settings import SECRET_KEY

if TYPE_CHECKING:
    from django.contrib.auth.models import User


def JSON(code: E = OK, data: Union[dict] = None, **kwargs) -> HttpResponse:
    response = code.body
    if data:
        response["data"] = data

    return HttpResponse(
        content=json.dumps(response, ensure_ascii=False, indent=2),
        content_type="application/json",
        **kwargs
    )


def issue_token(user: 'User') -> str:
    return jwt.encode({"id": user.id}, key=SECRET_KEY)

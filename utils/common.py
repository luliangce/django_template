import contextlib
import json
from typing import TYPE_CHECKING, Union, List, Tuple, Type

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from jose import jwt

from ecode import OK, E

if TYPE_CHECKING:
    from django.contrib.auth.models import User


def JSON(code: E = OK, data: Union[dict] = None, **kwargs) -> HttpResponse:
    response = code.body
    if data:
        response["data"] = data

    return HttpResponse(content=json.dumps(response,
                                           ensure_ascii=False,
                                           indent=2),
                        content_type="application/json",
                        **kwargs)


def issue_token(user: 'User') -> str:
    return jwt.encode({"id": user.id}, key=settings.SECRET_KEY)


@contextlib.contextmanager
def dontcare(exception=Exception):
    """
    通过上下文管理器捕获异常，减少请求方法中使用try:...except:...的次数
    >>> with dontcare():
    >>>     condition['param'] = 1 / 0
    >>> with dontcare():
    >>>     condition['user'] = 1
    """
    try:
        yield None
    except exception:
        ...


def get_lo(request: 'HttpRequest', limit=10, offset=0) -> (int, int):
    with dontcare():
        limit = int(request.GET['limit'])
    with dontcare():
        offset = int(request.GET['offset'])
    return offset, limit

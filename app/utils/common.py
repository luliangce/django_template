from typing import TYPE_CHECKING, Any, Generic, Optional, TypeVar

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from jose import jwt
from ninja.security import HttpBearer
from pydantic.fields import Field
from pydantic.generics import GenericModel

from ecode import E

if TYPE_CHECKING:
    from django.contrib.auth.models import User

T = TypeVar("T")


class R(GenericModel, Generic[T]):
    code: int = Field(200, description='返回状态码')
    msg: str = Field('成功', description='返回信息')
    data: Optional[T]

    def error(err: E) -> 'R':
        return R(**err.body)


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            claims = jwt.decode(token, settings.SECRET_KEY)
            request.user = User.objects.get(id=claims["id"])
            return request.user
        except:
            return None

    def __call__(self, request: HttpRequest) -> Optional[Any]:
        response = super().__call__(request)
        if not response:
            raise PermissionDenied
        return response


custom_auth = AuthBearer()


def issue_token(user: 'User') -> str:
    return jwt.encode({"id": user.id}, key=settings.SECRET_KEY)

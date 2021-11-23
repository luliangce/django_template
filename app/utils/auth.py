from typing import TYPE_CHECKING, Any, Optional

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from jose import jwt
from ninja.security import HttpBearer

if TYPE_CHECKING:
    from django.contrib.auth.models import User


class BearerAuth(HttpBearer):
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


bearer_auth = BearerAuth()


def issue_token(user: 'User') -> str:
    return jwt.encode({"id": user.id}, key=settings.SECRET_KEY)

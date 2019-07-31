from utils.common import JSON
from ecode import LOGINREQUIRED
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest
    from django.contrib.auth.models import User


class LoginRequired:

    def dispatch(self, request: 'HttpRequest', *args, **kwargs):
        user: 'User' = request.user
        if not user.is_authenticated:
            return JSON(code=LOGINREQUIRED)
        return super().dispatch(request, *args, **kwargs)

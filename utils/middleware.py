import json
from typing import TYPE_CHECKING

from django.contrib.auth.models import AnonymousUser, User
from jose import jwt

from ZRT.settings import SECRET_KEY

if TYPE_CHECKING:
    from django.http import HttpRequest


class JSONLoaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: 'HttpRequest'):
        try:
            request.json = json.loads(request.body)
        except:
            request.json = {}
        return self.get_response(request)


class JWTVerifyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: 'HttpRequest'):
        token = request.headers.get("Authorization")
        try:
            claims = jwt.decode(token.replace('Bearer ',''), SECRET_KEY)
            request.user = User.objects.get(id=claims["id"])
        except:
            request.user = AnonymousUser()

        return self.get_response(request)

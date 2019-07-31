from typing import TYPE_CHECKING

from django.contrib.auth import authenticate
from django.views.generic import View

from ecode import ERROR, NOTFOUND, OK
from utils.common import JSON, issue_token
from utils.mixin import LoginRequired

if TYPE_CHECKING:
    from django.http import HttpRequest


class Login(View):

    def post(self, request: "HttpRequest"):
        params: dict = request.json.copy()
        username = params.get("username")
        password = params.get("password")
        if not username or not password:
            return JSON(code=ERROR.inherit("用户名个密码为必填项"))
        user = authenticate(username=username, password=password)
        if not user:
            return JSON(code=ERROR.inherit("用户名或密码错误"))
        return JSON(code=OK,
                    data={"token": issue_token(user)}
                    )

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpRequest
from ninja import Router
from ninja.schema import Schema
from pydantic.fields import Field

from ecode import ERROR
from utils.common import R, custom_auth, issue_token

auth_router = Router(tags=['用户账户'])


class LoginParams(Schema):

    username: str = Field(None, description='用户名')
    password: str = Field(..., description='密码', min_length=8)


class LoginResponse(Schema):
    token: str


@auth_router.post('login', response=R[LoginResponse])
def login_impl(request: HttpRequest, body: LoginParams):
    user = authenticate(**body.dict())
    if user and user.is_authenticated:
        token = issue_token(user)
        return R(data=dict(token=token))
    return R.error(ERROR.inherit("账号密码不匹配"))


@auth_router.post("register")
def register_impl(request: HttpRequest, body: LoginParams):
    if User.objects.filter(username=body.username).exists():
        return R.error(ERROR.inherit("该用户名已经存在"))
    user = User(username=body.username)
    user.set_password(body.password)
    user.save()
    return R()

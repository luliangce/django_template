from authentication.schema.request import *
from common_schema import R
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpRequest
from ecode import ERROR
from ninja import Router
from utils import issue_token

auth_router = Router(tags=['用户账户'])


@auth_router.post('login', response=R[LoginResponse])
def login_impl(request: HttpRequest, body: LoginParams):
    user = authenticate(**body.dict())
    if user and user.is_authenticated:
        token = issue_token(user)
        return R(data=dict(token=token))
    return R.error(ERROR.inherit("账号密码不匹配"))


@auth_router.post("register", response=R)
def register_impl(request: HttpRequest, body: LoginParams):
    if User.objects.filter(username=body.username).exists():
        return R.error(ERROR.inherit("该用户名已经存在"))
    user = User(username=body.username)
    user.set_password(body.password)
    user.save()
    return R()

from ninja import Schema
from pydantic.fields import Field


class LoginParams(Schema):

    username: str = Field(None, description='用户名')
    password: str = Field(..., description='密码', min_length=8)


class LoginResponse(Schema):
    token: str

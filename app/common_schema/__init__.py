# Common Schemas

from typing import Generic, Optional, TypeVar

from ecode import E
from pydantic import Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class R(GenericModel, Generic[T]):
    code: int = Field(200, description='返回状态码')
    msg: str = Field('成功', description='返回信息')
    data: Optional[T] = None

    def error(err: E) -> 'R':
        return R(**err.body)

class E:
    def __init__(self, code: int, msg: str):
        """初始化返回模板,包含code和msg,返回时传入的不是code和msg,而是E对象. 

        Arguments:  

            code {int} -- 返回码中的code  
            msg {str} -- 返回给前端的msg
        """
        self.code = code
        self.msg = msg

    def inherit(self, msg: str) -> "E":
        """根据现有模板,变更返回信息之后生成一个新的模板  """
        return E(self.code, msg=msg)

    @property
    def body(self):
        return dict(
            code=self.code,
            msg=self.msg
        )

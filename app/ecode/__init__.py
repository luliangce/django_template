from ecode.basic import E

OK = E(200, "请求成功")
ERROR = E(400, "请求异常")
LOGINREQUIRED = E(403, "请先登录")
NOTFOUND = E(404, "资源不存在")

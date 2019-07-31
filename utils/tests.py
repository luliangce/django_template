import json

from django.test import TestCase

# Create your tests here.


class TestEcode(TestCase):

    def test_ecode(self):
        from ecode import OK
        ok_body = json.dumps(OK.body)
        ok_body_should_be = json.dumps({"code": 200, "msg": "请求成功"})
        self.assertEqual(ok_body, ok_body_should_be, "结果异常")

        modified_ok_body = json.dumps(OK.inherit("修改了").body)
        modified_ok_body_should_be = json.dumps({"code": 200, "msg": "修改了"})
        self.assertEqual(modified_ok_body, modified_ok_body_should_be, "修改异常")
from decimal import Decimal

import allure
import pytest
from utils.log_utils.logs_utils import *
from utils.other_utils.requests_utils import sendRequest


@allure.epic("openapi")
@allure.feature("用户登录操作")
class TestOpen:

    def setup_class(self):
        pass

    @allure.story("正常用户登录")
    def test_user_01(self):
        url = "http://192.168.1.198:9900/api-uaa/oauth/token?email=110@qq.com&password=123456&grant_type=email_password&account_type=org"
        headers = {
            "Authorization": "Basic d2ViQXBwOndlYkFwcA =="
        }
        message = sendRequest(url=url, method="post", headers=headers)
        # message[]
        # 验证token
        pass

    @allure.story("邮箱错误验证错误，密码正常")
    def test_not_email_01(self):
        print("邮箱错误验证错误，密码正常")
        assert 1 == 1

    @allure.story("邮箱正确，密码错误")
    def test_not_pwd_01(self):
        pass


if __name__ == '__main__':
    # pytest.main(['test_get_user_info.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
    pytest.main(['test_openapi_login.py', '-s'])

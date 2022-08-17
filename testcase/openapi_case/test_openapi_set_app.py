import json

import allure
import pytest
from utils.log_utils.logs_utils import *
from utils.other_utils.requests_utils import sendRequest

access_token = {}
email = "11@qq.com"

@allure.epic("openapi")
@allure.feature("创建平台数字身份")
class TestLogin_info:

    def setup_class(self):
        url = ConfigHandler.localhost + "/api-uaa/oauth/token?email="+email+"&password=123456&grant_type=email_password&account_type=org"
        headers = {
            "Authorization": "Basic d2ViQXBwOndlYkFwcA==",
            'Content-Type': 'application/json'
        }

        message = sendRequest(url=url, method="post", headers=headers)
        access_token["access_token"] = message['datas']['access_token']

    def teardown_class(self):
        # close
        pass

    @allure.story("创建平台数字身份")
    def test_set_platform(self):
        bear = access_token['access_token']
        url = ConfigHandler.localhost + "/api-manager/platform/digital"
        headers = {
            "Authorization": "Bearer " + bear,
            'Content-Type': 'application/json',
            "Content-Length": '194'
        }
        data = {"email": email, "headPortrait": "1", "id": 3, "nickName": "111111111111111111111111",
                "remark": "创建操作"}

        message = sendRequest(url=url, method="post", headers=headers, data=json.dumps(data))
        assert message["resp_msg"] == "保存成功"

    @allure.story("接入用户数据创建用户数字身份")
    def test_user_to_wallet_01(self):
        pass


if __name__ == '__main__':
    # pytest.main(['test_get_user_info.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
    pytest.main(['test_openapi_set_app.py', '-s'])

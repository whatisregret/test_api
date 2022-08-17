import json

from utils.other_utils.requests_utils import sendRequest
from config.setting import ConfigHandler

url = ConfigHandler.localhost + "/api-uaa/oauth/token?email=11@qq.com&password=123456&grant_type=email_password&account_type=org"
headers = {
    "Authorization": "Basic d2ViQXBwOndlYkFwcA==",
    'Content-Type': 'application/json'
}

message = sendRequest(url=url, method="post", headers=headers)
access_token = message['datas']['access_token']

print(message)
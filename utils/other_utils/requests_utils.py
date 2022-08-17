import requests
from utils.log_utils.logs_utils import *


def sendRequest(url, method, params=None, data=None,
                headers=None, json=None, cookies=None, timeout=5):
    """
    :param url: 接口请求地址
    :param method: 接口请求方法：get/post或其他
    :param params: url额外参数，字典或字节流格式（多用于字典格式，字节流的话，多用于文件操作）
    :param data:   字典、字节序列或文件对象（多用于字典）
    :param headers: 请求头信息，字典形式
    :param json:    JSON格式的数据，作为参数传递
    :param cookies:  cookies信息，str类型
    :param  timeout:   设定超时时间，秒为单位
    :return: requests.Response.json()
    """
    responseResult = None
    new_method = method.lower()
    if new_method == 'get':
        INFO.logger.info("正在发送get请求，请求地址：{}， 请求参数{}".format(url, params))
        responseResult = requests.get(url=url, params=params, headers=headers, timeout=timeout)
    elif new_method == "post":
        INFO.logger.info("正在发送POST请求，请求地址：{}， 请求参数{}".format(url, data))
        responseResult = requests.post(url=url, data=data, headers=headers, cookies=cookies, timeout=timeout)

    return responseResult.json()


import socket
import os


def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    _s = None
    try:
        _s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _s.connect(('8.8.8.8', 80))
        l_host = _s.getsockname()[0]
    finally:
        _s.close()

    return l_host


def get_os_sep():
    """
    判断不同的操作系统的路径
    :return: windows 返回 "\", linux 返回 "/"
    """
    return os.sep

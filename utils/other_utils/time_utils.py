import time


def now_time_year():
    """
    获取当前时间, 日期格式: 2021
    :return:
    """
    localtime = time.strftime("%Y", time.localtime())
    return localtime


def now_time_month():
    """
    获取当前时间, 日期格式: 2021-12
    :return:
    """
    localtime = time.strftime("%Y-%m", time.localtime())
    return localtime


def now_time_day():
    """
    获取当前时间, 日期格式: 2021-12-11
    :return:
    """
    localtime = time.strftime("%Y-%m-%d", time.localtime())
    return localtime


def now_time_hour():
    """
    获取当前时间, 日期格式: 2021-12-11-18
    :return:
    """
    localtime = time.strftime("%Y-%m-%d-%H", time.localtime())
    return localtime


def now_time_minute():
    """
    获取当前时间, 日期格式: 2021-12-11-18-22
    :return:
    """
    localtime = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
    return localtime


def now_time_second():
    """
    获取当前时间, 日期格式: 2022-08-08-18-22-50
    :return:
    """
    localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    return localtime


if __name__ == '__main__':
    print(now_time_second())

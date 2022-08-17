#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2021/11/26 18:27
# @Author : 余少琪
"""
mysql 封装，支持 增、删、改、查
"""

import datetime
import decimal
from warnings import filterwarnings
import pymysql
from typing import Text
from utils.log_utils.logs_utils import ERROR

# 忽略 Mysql 告警信息
filterwarnings("ignore", category=pymysql.Warning)

host = '139.159.161.13'
port = 3306
user = 'handian'
passwd = 'YBI8*VugQ'
db = 'ul_wallet'
charset = 'utf8'


class MysqlDB:
    """ mysql 封装 """

    def __init__(self):
        try:
            # 建立数据库连接
            self.conn = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
                charset=charset
            )

            # 使用 cursor 方法获取操作游标，得到一个可以执行sql语句，并且操作结果为字典返回的游标
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except AttributeError as error:
            ERROR.logger.error("数据库连接失败，失败原因 %s", error)

    def __del__(self):
        try:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()
        except AttributeError as error:
            ERROR.logger.error("数据库连接失败，失败原因 %s", error)

    def query(self, sql, state="all"):
        """
            查询
            :param sql:
            :param state:  all 是默认查询全部
            :return:
            """
        try:
            self.cur.execute(sql)
            if state == "all":
                # 查询全部
                data = self.cur.fetchall()
            else:
                # 查询单条
                data = self.cur.fetchone()
            return data
        except AttributeError as error_data:
            ERROR.logger.error("数据库连接失败，失败原因 %s", error_data)

    def execute(self, sql: Text):
        """
            更新 、 删除、 新增
            :param sql:
            :return:
            """
        try:
            # 使用 execute 操作 sql
            rows = self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
            return rows
        except AttributeError as error:
            ERROR.logger.error("数据库连接失败，失败原因 %s", error)
            # 如果事务异常，则回滚数据
            self.conn.rollback()

    @classmethod
    def sql_data_handler(cls, query_data, data):
        """
        处理部分类型sql查询出来的数据格式
        @param query_data: 查询出来的sql数据
        @param data: 数据池
        @return:
        """
        # 将sql 返回的所有内容全部放入对象中
        for key, value in query_data.items():
            if isinstance(value, decimal.Decimal):
                data[key] = float(value)
            elif isinstance(value, datetime.datetime):
                data[key] = str(value)
            else:
                data[key] = value
        return data

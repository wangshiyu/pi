# encoding: utf-8
# !/usr/bin/python3
from pi_client.web.web_service.models.dto.BaseDTO import BaseDTO

"""
UserTcpAddress 返回对象
"""


class UserTcpAddressDTO(BaseDTO):
    userId = None  # 用户id
    address = None  # 地址
    connect = False  # 是否连接

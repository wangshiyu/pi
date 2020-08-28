# encoding: utf-8
# !/usr/bin/python3
"""
权限缓存实体
"""


class Auth:
    userName = None
    password = None
    authority = None

    def __init__(self, userName, password, authority):
        self.userName = userName
        self.password = password
        self.authority = authority

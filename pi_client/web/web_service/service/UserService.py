# encoding: utf-8
# !/usr/bin/python3
from pi_client.web.web_service.service.BaseService import BaseService
from pi_db.client.dao.UserDao import UserDao

"""用户服务"""


class UserService(BaseService):
    baseDao = UserDao()

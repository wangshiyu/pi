# encoding: utf-8
# !/usr/bin/python3
from pi_client.web.web_service.service.BaseService import BaseService
from pi_db.client.dao.UserManipulatePageDao import UserManipulatePageDao

"""用户操控页面服务"""


class UserManipulatePageService(BaseService):
    baseDao = UserManipulatePageDao()

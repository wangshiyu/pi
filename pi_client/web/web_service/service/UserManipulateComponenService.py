# encoding: utf-8
# !/usr/bin/python3
from pi_client.web.web_service.service.BaseService import BaseService
from pi_db.client.dao.UserManipulateComponenDao import UserManipulateComponenDao

"""用户操控页面组件服务"""


class UserManipulateComponenService(BaseService):
    baseDao = UserManipulateComponenDao()
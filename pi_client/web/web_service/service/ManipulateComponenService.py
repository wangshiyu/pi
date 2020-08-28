# encoding: utf-8
# !/usr/bin/python3
from pi_client.web.web_service.service.BaseService import BaseService
from pi_db.client.dao.ManipulateComponenDao import ManipulateComponenDao

"""操控组件服务"""


class ManipulateComponenService(BaseService):
    baseDao = ManipulateComponenDao()

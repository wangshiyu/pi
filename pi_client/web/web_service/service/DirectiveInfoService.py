# encoding: utf-8
# !/usr/bin/python3
from pi_client.web.web_service.service.BaseService import BaseService
from pi_db.common.dao.DirectiveInfoDao import DirectiveInfoDao

"""驱动配置信息服务"""


class DirectiveInfoService(BaseService):
    baseDao = DirectiveInfoDao()
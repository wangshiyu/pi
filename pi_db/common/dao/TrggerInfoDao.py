# encoding: utf-8
# !/usr/bin/python3
from pi_db.common.dao.BaseDao import BaseDao
from pi_db.common.entity.TrggerInfoEntity import TrggerInfoEntity

"""
触发器Dao
"""


class TrggerInfoDao(BaseDao):
    entityClass = TrggerInfoEntity

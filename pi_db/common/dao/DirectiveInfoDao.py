# encoding: utf-8
# !/usr/bin/python3
from pi_db.common.dao.BaseDao import BaseDao
from pi_db.common.entity.DirectiveInfoEntity import DirectiveInfoEntity
from pi_db.cache.TableCache import directiveInfoMap
import time

"""
驱动配置信息Dao
"""


class DirectiveInfoDao(BaseDao):
    entityClass = DirectiveInfoEntity

    def getById(self, id):
        result = directiveInfoMap.get(id)
        if result is None:
            return super().getById(id)
        result.cacheCreateTime = time.time()
        return result
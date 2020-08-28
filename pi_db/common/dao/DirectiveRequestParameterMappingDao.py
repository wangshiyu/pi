# encoding: utf-8
# !/usr/bin/python3
from pi_db.common.dao.BaseDao import BaseDao
from pi_db.common.entity.DirectiveRequestParameterMappingEntity import DirectiveRequestParameterMappingEntity
from pi_db.cache.TableCache import directiveRequestParameterMappingMap
import time

"""
驱动请求参数映射Dao
"""


class DirectiveRequestParameterMappingDao(BaseDao):
    entityClass = DirectiveRequestParameterMappingEntity

    def getById(self, id):
        result = directiveRequestParameterMappingMap.get(id)
        if result is None:
            return super().getById(id)
        result.cacheCreateTime = time.time()
        return result
# encoding: utf-8
# !/usr/bin/python3
from pi_db.common.dao.BaseDao import BaseDao
from pi_db.common.entity.DirectiveHardwareEntity import DirectiveHardwareEntity
from pi_db.cache.TableCache import directiveHardwareMap
import time

"""
驱动硬件映射Dao
"""


class DirectiveHardwareDao(BaseDao):
    entityClass = DirectiveHardwareEntity

    def getById(self, id):
        result = directiveHardwareMap.get(id)
        if result is None:
            return super().getById(id)
        result.cacheCreateTime = time.time()
        return result
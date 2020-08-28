# encoding: utf-8
# !/usr/bin/python3
from pi_db.common.dao.BaseDao import BaseDao
from pi_db.common.entity.DirectiveCommadAlgorithmEntity import DirectiveCommadAlgorithmEntity
from pi_db.cache.TableCache import directiveCommadAlgorithmMap
import time

"""
驱动命令算法Dao
"""


class DirectiveCommadAlgorithmDao(BaseDao):
    entityClass = DirectiveCommadAlgorithmEntity

    def getById(self, id):
        result = directiveCommadAlgorithmMap.get(id)
        if result is None:
            return super().getById(id)
        result.cacheCreateTime = time.time()
        return result
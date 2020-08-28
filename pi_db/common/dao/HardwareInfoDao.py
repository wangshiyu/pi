# encoding: utf-8
# !/usr/bin/python3
from pi_db.common.dao.BaseDao import BaseDao
from pi_db.common.entity.HardwareInfoEntity import HardwareInfoEntity
from pi_db.cache.TableCache import hardwareInfoMap
import time

"""
硬件信息Dao
"""


class HardwareInfoDao(BaseDao):
    entityClass = HardwareInfoEntity

    def getById(self, id):
        result = hardwareInfoMap.get(id) # 先从缓存中获取
        if result is None:
            return super().getById(id)
        result.cacheCreateTime = time.time()
        return result
# encoding: utf-8
# !/usr/bin/python3

from pi_db.common.entity.TrggerInfoEntity import TrggerInfoEntity
from pi_db.common.dao.TrggerInfoDao import TrggerInfoDao
from pi_common.config.Config import Config, ConfigEnum, ConfigValueEnum
from pi_drive.cache.StructureJsonCache import triggerInfoMap


"""
触发器数据加载
"""
trggerInfoDao = TrggerInfoDao()
trggerInfoEntity = TrggerInfoEntity()
if Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.client):
    trggerInfoEntity.loadType = 2
elif Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.server):
    trggerInfoEntity.loadType = 1
else:
    pass

listData = trggerInfoDao.getListByEntity(trggerInfoEntity)
if len(listData) != 0:
    for item in listData:
        triggerInfoMap.put(item.triggerTaskId, item)

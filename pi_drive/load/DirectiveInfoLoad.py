# encoding: utf-8
# !/usr/bin/python3

from pi_db.common.dao.DirectiveInfoDao import DirectiveInfoDao
from pi_db.common.entity.DirectiveInfoEntity import DirectiveInfoEntity
from pi_drive.cache.StructureJsonCache import codeDict
from pi_common.config.Config import ConfigEnum, Config
from pi_drive.processor.CodeDictProcessor import CodeDictProcessor

"""
驱动配置信息加载
"""
directiveInfoDao = DirectiveInfoDao()
directiveInfoEntity = DirectiveInfoEntity()
codeDictProcessor = CodeDictProcessor()
directiveInfoEntity.pattern = Config.getConfig(ConfigEnum.PATTERN)


def codeDictAddCache(directiveIdentificationList):
    if len(directiveIdentificationList) != 0:
        for i in directiveIdentificationList:
            directiveInfoEntity.identification = i
            list_ = directiveInfoDao.getListByEntity(directiveInfoEntity)
            if len(list_) != 0:
                for item in list_:
                    dict = codeDictProcessor.getCodeDict(item)
                    codeDict.put(i, dict)

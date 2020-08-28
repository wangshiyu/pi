# encoding: utf-8
# !/usr/bin/python3

from pi_db.common.dao.DirectiveHardwareDao import DirectiveHardwareDao
from pi_db.common.entity.DirectiveHardwareEntity import DirectiveHardwareEntity
from pi_common.config.Config import Config, ConfigValueEnum, ConfigEnum
from pi_drive.processor.DirectiveCommadAlgorithmParametersDictProcessor import \
    DirectiveCommadAlgorithmParametersDictProcessor
from pi_drive.processor.TriggerTaskProcessor import TriggerTaskProcessor, TriggerTaskStart
from pi_drive.load.DirectiveInfoLoad import codeDictAddCache
from pi_drive.cache.StructureJsonCache import triggerInfoMap, modularParametersDict, \
    directiveCommadAlgorithmJsonMap
from pi_common.constant.DictKeyConstant import DictKeyConstant
from pi_drive.cache.DriveCache import directiveParameterMap, modularToTaskId

"""
驱动硬件映射加载
"""
directiveHardwareDao = DirectiveHardwareDao()
directiveHardwareEntity = DirectiveHardwareEntity()
triggerTaskProcessor = TriggerTaskProcessor()
directiveCommadAlgorithmParametersDictProcessor = DirectiveCommadAlgorithmParametersDictProcessor()
if Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.client):
    directiveHardwareEntity.calculation = ConfigValueEnum.client.value
elif Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.server):
    directiveHardwareEntity.calculation = ConfigValueEnum.server.value
else:
    pass
list_ = directiveHardwareDao.getListByEntity(directiveHardwareEntity)

if len(list_) != 0:
    directiveIdentificationList = list()
    for item in list_:
        directiveCommadAlgorithmJsonStr = item.directiveCommadAlgorithmJson
        directiveCommadAlgorithmJsonStr = directiveCommadAlgorithmJsonStr.replace('\'', '\"')
        print(directiveCommadAlgorithmJsonStr)
        list = directiveCommadAlgorithmParametersDictProcessor.getDirectiveCommadAlgorithmJson(
            directiveCommadAlgorithmJsonStr)
        directiveCommadAlgorithmJsonMap.put(item.modularIdentification, list)
        directiveIdentificationList.append(item.directiveIdentification)
        dict_ = directiveParameterMap.get(item.modularIdentification)
        if dict_ is None:
            dict_ = {}
            directiveParameterMap.put(item.modularIdentification, dict_)
        dict_[DictKeyConstant.MODULAR_IDENTIFICATION] = item.modularIdentification
        modularParametersDict.put(item.modularIdentification, dict_)
        """模块对应触发器"""
        modularToTaskId.put(item.modularIdentification, item.triggerTaskId)
        """加载触发器"""
        triggerInfoData = triggerInfoMap.get(item.triggerTaskId)
        triggerTaskProcessor.triggerTaskBuild(triggerInfoData, dict_)  ## 加载触发器
    codeDictAddCache(directiveIdentificationList)
    TriggerTaskStart.triggerTaskStart()

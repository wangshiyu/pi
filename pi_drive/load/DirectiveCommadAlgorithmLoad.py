# encoding: utf-8
# !/usr/bin/python3

from pi_db.common.dao.DirectiveCommadAlgorithmDao import DirectiveCommadAlgorithmDao
from pi_db.common.entity.DirectiveCommadAlgorithmEntity import DirectiveCommadAlgorithmEntity
from pi_common.config.Config import Config, ConfigEnum, ConfigValueEnum
from pi_drive.cache.DriveCache import directiveCommadAlgorithmMap, directiveCommadAlgorithmLoadType
from pi_drive.processor.InputParameterTypeDictProcessor import InputParameterTypeDictProcessor
from pi_drive.cache.StructureJsonCache import inputParameterTypeJsonMap
from pi_common.constant.enums.LoadTypeEnum import LoadTypeEnum
from pi_common.constant.DictKeyConstant import DictKeyConstant

"""
驱动命令算法加载
"""
inputParameterTypeDictProcessor = InputParameterTypeDictProcessor()
directiveCommadAlgorithmDao = DirectiveCommadAlgorithmDao()
directiveCommadAlgorithmEntity = DirectiveCommadAlgorithmEntity()
if Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.client):
    directiveCommadAlgorithmEntity.loadType = 2
elif Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.server):
    directiveCommadAlgorithmEntity.loadType = 1
else:
    pass

list = directiveCommadAlgorithmDao.getListByEntity(directiveCommadAlgorithmEntity)
if len(list) != 0:
    for item in list:
        if item.loadType == LoadTypeEnum.Client.value:
            directiveCommadAlgorithmLoadType.put(item.algorithmSign + DictKeyConstant.CLIENT_SUFFIX, True)
        elif item.loadType == LoadTypeEnum.Server.value:
            directiveCommadAlgorithmLoadType.put(item.algorithmSign + DictKeyConstant.SERVER_SUFFIX, True)
        directiveCommadAlgorithmMap.put(item.algorithmSign, item)
        inputParameterTypeJson = item.inputParameterTypeJson
        inputParameterTypeJson = inputParameterTypeJson.replace('\'', '\"')
        print(inputParameterTypeJson)
        dict = inputParameterTypeDictProcessor.getInputParameterTypeJSON(inputParameterTypeJson)
        inputParameterTypeJsonMap.put(item.algorithmSign, dict)

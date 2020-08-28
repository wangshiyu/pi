# encoding: utf-8
# !/usr/bin/python3

from pi_db.common.dao.DirectiveRequestParameterMappingDao import DirectiveRequestParameterMappingDao
from pi_db.common.entity.DirectiveRequestParameterMappingEntity import DirectiveRequestParameterMappingEntity
from pi_drive.structure.toJson.directive_request_parameter_mapping.ParametersMappingJson import ParametersMappingJson
from pi_drive.cache.StructureJsonCache import parametersMappingJsonMap
from pi_common.config.Config import ConfigEnum,Config,ConfigValueEnum

"""
参数映射加载
"""
if Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.client):
    directiveRequestParameterMappingDao = DirectiveRequestParameterMappingDao()
    directiveRequestParameterMappingEntity = DirectiveRequestParameterMappingEntity()
    parametersMappingJson = ParametersMappingJson()
    listDate = directiveRequestParameterMappingDao.getListByEntity(directiveRequestParameterMappingDao)
    if len(listDate) != 0:
        for item in listDate:
            parametersMapping = parametersMappingJson.jsonToObj(item.parametersMappingJson)
            parametersMappingJsonMap.put(item.modularIdentification,parametersMapping)

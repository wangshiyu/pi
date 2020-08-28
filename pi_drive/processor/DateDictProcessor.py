# encoding: utf-8
# !/usr/bin/python
from pi_common.constant.DictKeyConstant import DictKeyConstant
from pi_drive.processor.CodeDictProcessor import CodeDictProcessor
from pi_drive.processor.DirectiveCommadAlgorithmParametersDictProcessor import \
    DirectiveCommadAlgorithmParametersDictProcessor
from pi_drive.processor.TriggerTaskProcessor import TriggerTaskProcessor
from pi_drive.structure.toJson.directive_hardware.ChannelJson import ChannelJson
from pi_db.common.dao.DirectiveCommadAlgorithmDao import DirectiveCommadAlgorithmDao
from pi_db.common.dao.DirectiveInfoDao import DirectiveInfoDao
from pi_db.common.entity.DirectiveInfoEntity import DirectiveInfoEntity
from pi_common.config.Config import Config,ConfigEnum

"""
数据字典处理器
"""


class DateDictProcessor:
    directiveInfoDao = None
    codeDictProcessor = None
    triggerTaskProcessor = None
    directiveCommadAlgorithmParametersDictProcessor = None
    channelJson = None

    def __init__(self):
        self.directiveInfoDao = DirectiveInfoDao()
        self.codeDictProcessor = CodeDictProcessor()
        self.directiveCommadAlgorithmParametersDictProcessor = DirectiveCommadAlgorithmParametersDictProcessor()
        self.channelJson = ChannelJson()
        self.triggerTaskProcessor = TriggerTaskProcessor()

    def getDict(self, directiveHardware):
        directiveInfoEntity = DirectiveInfoEntity()
        directiveInfoEntity.pattern = Config.getConfig(ConfigEnum.PATTERN)
        directiveInfoEntity.identification = directiveHardware.directiveIdentification
        list = self.directiveInfoDao.getListByEntity(directiveInfoEntity)
        directiveInfoEntity = list[0]
        ##dict = self.codeDictProcessor.getCodeDict(directiveInfoEntity)
        ##dict[DictKeyConstant.DIRECTIVE_COMMAD_ALGORITHM_JSON] = directiveHardware.directiveCommadAlgorithmJson
        ##dict[DictKeyConstant.TRIGGER_TASK_JSON] = directiveHardware.triggerTaskJson
        ##self.directiveCommadAlgorithmParametersDictProcessor.getParamsDict(dict)  ##获取触发任务
        channelDict = self.channelJson.jsonToObj(directiveHardware.channelJson)
        dict[DictKeyConstant.CHANNEL_DICT] = channelDict
        return dict

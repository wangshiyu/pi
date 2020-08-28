# encoding: utf-8
# !/usr/bin/python

from pi_common.constant.DictKeyConstant import DictKeyConstant
from pi_common.log.LoggingFactory import logger
from pi_common.util.ReflexUtil import ReflexUtil
from pi_drive.cache.DriveCache import *
from pi_drive.cache.StructureJsonCache import *
from pi_drive.processor.DirectiveCommadAlgorithmParametersDictProcessor import \
    DirectiveCommadAlgorithmParametersDictProcessor

directiveCommadAlgorithmParametersDictProcessor = DirectiveCommadAlgorithmParametersDictProcessor()

"""
核心处理器
"""


class CoreProcessor:

    @staticmethod
    def execute(dict):
        commandsAll = list()
        modularIdentification = dict.get(DictKeyConstant.MODULAR_IDENTIFICATION)
        directiveCommadAlgorithmList = directiveCommadAlgorithmJsonMap.get(modularIdentification)
        if len(directiveCommadAlgorithmList) != 0:
            directiveCommadAlgorithmDict = directiveCommadAlgorithmParametersDictProcessor.getParamsDict(
                directiveCommadAlgorithmList, dict)
            for key in directiveCommadAlgorithmDict.keys():
                codeDataDict = codeDict.get(key)
                for paramDict in directiveCommadAlgorithmDict.get(key):
                    paramDict[DictKeyConstant.CODE_DATA] = codeDataDict
                    directiveCommadAlgorithm = directiveCommadAlgorithmMap.get(key)
                    commands = None
                    if directiveCommadAlgorithm is None:
                        return None
                    else:
                        if directiveCommadAlgorithm.handleModel != None and directiveCommadAlgorithm.handleModel != '':
                            try:
                                model_path, class_name = directiveCommadAlgorithm.handleModel.rsplit(".", 1)
                                obj = ReflexUtil.modelGetExample(model_path, class_name)
                                commands = obj.buildDirectiveCommand(paramDict)
                            except Exception as e:
                                errorStr = 'directiveCommadAlgorithm.handleModel Algorithm load fail!  algorithm_sign is:' + key + 'e:' + str(
                                    e)
                                logger.error(errorStr)
                                raise RuntimeError(errorStr)
                        elif directiveCommadAlgorithm.commandHandle != None and directiveCommadAlgorithm.handleModel != '':
                            result = {}
                            try:
                                reguest = paramDict
                                exec(directiveCommadAlgorithm.commandHandle)
                                commands = result.get(DictKeyConstant.COMMANDS)
                            except Exception as e:
                                errorStr = 'directiveCommadAlgorithm.commandHandle Algorithm load fail!  algorithm_sign is:' + key + 'e:' + str(
                                    e)
                                logger.error(errorStr)
                                raise RuntimeError(errorStr)
                            if commands is None:
                                errorStr = 'directiveCommadAlgorithm.commandHandle Algorithm commands is None! algorithm_sign is:' + key
                                logger.error(errorStr)
                                raise RuntimeError(errorStr)
                        else:
                            errorStr = 'directiveCommadAlgorithm Algorithm is None! algorithm_sign is:' + key
                            logger.error(errorStr)
                            raise RuntimeError(errorStr)

                        if commands is not None and len(commands) >= 0:
                            for command in commands:
                                commandsAll.append(command)

                return commandsAll
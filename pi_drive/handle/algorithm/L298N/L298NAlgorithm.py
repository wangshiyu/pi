# encoding: utf-8
# !/usr/bin/python3
from pi_common.command_set.DirectiveCommand import DirectiveCommand
from pi_common.constant.AlgorithmConstant import *
from pi_common.constant.DictKeyConstant import *
from pi_common.constant.enums.CommandTypeEnum import CommandTypeEnum
from pi_drive.handle.DriveCommand.CommandHandle import CommandHandle

""" L298N命令处理器"""


class L298NAlgorithm(CommandHandle):
    """
    构建驱动命令
    """

    @staticmethod
    def buildDirectiveCommand(dict):
        l298NCommandParams = L298NAlgorithm.culation(dict)
        if l298NCommandParams is None:
            return None
        commands = list()
        command = DirectiveCommand()
        command.directiveCommandCode = dict.get(AlgorithmConstant.CODE_MAPPING_COMPLETE)
        command.queueName = dict.get(AlgorithmConstant.EXECUTE_QUEUE_ENAME)
        complete = dict.get(AlgorithmConstant.CODE_MAPPING_COMPLETE)
        command.parameter = l298NCommandParams
        if complete != True:
            codeDict = dict.get(DictKeyConstant.CODE_DATA)
            command.importCodes = codeDict.get(AlgorithmConstant.IMPORT_CODES)
        command.methodName = dict.get(AlgorithmConstant.METHOD)
        command.commandType = CommandTypeEnum.pi_directive._value_
        commands.append(command)
        return commands

    """
    计算行动角度
    """

    @staticmethod
    def culation(dict):
        y = dict.get('Y')  # Y值
        ruler_y = dict.get('RULER_Y')  # 标尺

        paramList = list()
        proportion = abs(y) / ruler_y

        if y > 0.0:
            paramList.append(1)
        elif y < 0.0:
            paramList.append(-1)
        else:
            return None

        sleep_time1 = float(proportion * dict.get('CAE_MOVE_DRIVING_TIME'))
        sleep_time2 = float(dict.get('CAE_MOVE_DRIVING_TIME') - sleep_time1)

        paramList.append(round(sleep_time1,3))
        paramList.append(round(sleep_time2,3))

        return paramList

# encoding: utf-8
# !/usr/bin/python3
import importlib
from pi_common.log.LoggingFactory import logger
from pi_drive.cache.DriveCache import directiveParameterMap
from pi_common.util.DictUtil import dictCopy

"""
参数同步处理器
"""


class DirectiveParameterSynchronizationProcessor:

    """同步命令处理"""
    @staticmethod
    def doHandle(command):
       key= command.key
       dictDate = command.value
       oldDict = directiveParameterMap.get(key)
       dictCopy(dictDate,oldDict)

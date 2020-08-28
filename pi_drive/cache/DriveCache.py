# encoding: utf-8
# !/usr/bin/python3
from pi_common.util.structure.Map import Map

"""触发任务命令处理器"""
triggerTaskCommandHandle = None


def setTriggerTaskCommandHandle(obj):
    global triggerTaskCommandHandle
    triggerTaskCommandHandle = obj


def getTriggerTaskCommandHandle():
    return triggerTaskCommandHandle


"""驱动命令算法缓存"""
directiveCommadAlgorithmMap = Map()

"""驱动参数字段"""
directiveParameterMap = Map()

"""
触发器缓存
"""
taskIdTotriggerTaskMap = Map()

"""
模块对应触发器ID
"""
modularToTaskId = Map()

"""驱动算法加载类型缓存"""
directiveCommadAlgorithmLoadType = Map()

# encoding: utf-8
# !/usr/bin/python3
from pi_common.component.task_queue.TaskQueue import TaskQueue
from pi_common.config.Config import Config, ConfigValueEnum, ConfigEnum
from pi_common.util.structure import Map
from pi_server.core.execute_handle.ReturnResultExecuteHandle import ReturnResultExecuteHandle

"""
用于存储socketServer建立的通道
"""
tcpServiceChannelMapCache = Map.Map()

"""
用于存储驱动映射
"""
codeMappingMapCache = Map.Map()

"""
用于存储驱动队列结构
"""
directiveCommandMapCache = Map.Map()

"""结果返回队列"""
resultTaskQueue = None
if Config.eq(ConfigEnum.RUN_TYPE,ConfigValueEnum.server):
    resultTaskQueue = TaskQueue("returnResult", ReturnResultExecuteHandle())


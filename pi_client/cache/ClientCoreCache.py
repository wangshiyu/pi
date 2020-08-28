# encoding: utf-8
# !/usr/bin/python3

from pi_client.core.ClientCore import ClientCore
from pi_common.config.Config import Config, ConfigValueEnum, ConfigEnum
from pi_drive.cache.DriveCache import *
from pi_client.core.external_handle.ClientTriggerTaskCommandHandle import ClientTriggerTaskCommandHandle
from pi_common.component.task_queue.TaskQueue import TaskQueue
from pi_client.core.handle.ParameterSynchronization import ParameterSynchronization

"""
客户端核心
"""

clientCore = None
parameterSynchronizationTaskQueue = None
if Config.eq(ConfigEnum.RUN_TYPE, ConfigValueEnum.client):
    parameterSynchronizationTaskQueue = TaskQueue('parameterSynchronizationTaskQueue',ParameterSynchronization())
    clientCore = ClientCore()
    setTriggerTaskCommandHandle(ClientTriggerTaskCommandHandle())

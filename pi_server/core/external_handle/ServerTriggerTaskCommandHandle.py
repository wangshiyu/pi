# encoding: utf-8
# !/usr/bin/python3
from pi_drive.task.handle.TriggerTaskCommandHandle import TriggerTaskCommandHandle
from pi_server.core.execute_processor.ServerExecuteSelector import ServerExecuteSelector

"""
服务端触发任务命令处理器
"""


class ServerTriggerTaskCommandHandle(TriggerTaskCommandHandle):
    serverExecuteSelector = ServerExecuteSelector()

    def addDictData(self, dict):
        self.serverExecuteSelector.addMsg(dict)


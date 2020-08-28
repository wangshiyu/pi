# encoding: utf-8
# !/usr/bin/python3

from pi_common.component.task_queue.TaskQueueExecute import TaskQueueExecute
from pi_common.communication.msg.TcpMsg import TcpMsg
from pi_common.communication.tcp.send.TcpSendMsg import TcpSendMsg

"""
结果返回执行器
"""


class ReturnResultExecuteHandle(TaskQueueExecute):

    def execute(self, task):
        msg = TcpMsg()
        # msg.return_ = task.return_
        # msg.originalMsgId = task.originalMsgId
        msg.data = task.date
        msg.msgType = task.msgType
        TcpSendMsg.sendMsg(msg)
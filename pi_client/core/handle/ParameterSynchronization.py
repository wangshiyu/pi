# encoding: utf-8
# !/usr/bin/python3

from pi_client.cache.PiClientCache import tcpServiceChannelMapCache
from pi_common.component.task_queue.TaskQueueExecute import TaskQueueExecute
from pi_common.communication.tcp.client.TcpSocketClientMagSend import TcpSocketClientMagSend
from pi_common.command_set.ParameterSynchronizationCommand import ParameterSynchronizationCommand
from pi_common.constant.enums.CommandTypeEnum import CommandTypeEnum
from pi_common.constant.enums.ParameterSynchronizationTypeEnum import ParameterSynchronizationTypeEnum

"""
参数同步执行器
"""


class ParameterSynchronization(TaskQueueExecute):

    def execute(self, task):
        addresss = task.addresss
        if len(addresss) != 0:
            for address in addresss:
                channel = tcpServiceChannelMapCache.get(address)
                if channel is not None:
                    commands = list()
                    command = ParameterSynchronizationCommand()
                    command.commandType = CommandTypeEnum.pi_parameter_synchronization.value
                    command.parameterSynchronizationType = ParameterSynchronizationTypeEnum.DIRECTIVE.value
                    command.key = task.key
                    command.value = task.value
                    commands.append(command)
                    try:
                        TcpSocketClientMagSend.sendMsgCommand(channel, commands)
                    except Exception as e:
                        print("参数同步失败！！！"+e)
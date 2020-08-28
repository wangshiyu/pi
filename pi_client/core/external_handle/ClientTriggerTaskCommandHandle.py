# encoding: utf-8
# !/usr/bin/python3
from pi_drive.task.handle.TriggerTaskCommandHandle import TriggerTaskCommandHandle
from pi_common.communication.tcp.client.TcpSocketClientMagSend import TcpSocketClientMagSend
from pi_client.cache.PiClientCache import tcpServiceChannelMapCache
from pi_common.constant.DictKeyConstant import DictKeyConstant

"""
客户端触发任务命令处理器
"""


class ClientTriggerTaskCommandHandle(TriggerTaskCommandHandle):

    def addDictData(self, dict):
        addresss = dict.get(DictKeyConstant.ADDRESSS)
        if addresss is not None and isinstance(addresss,list) and len(addresss) > 0:
            for address in addresss:
                if address is None or address =='':return
                tcpChannelCacheEntity = tcpServiceChannelMapCache.get(address.strip())
                if tcpChannelCacheEntity != None:
                    TcpSocketClientMagSend.sendMsgCommand(tcpChannelCacheEntity.tcpSocketClient.channel,
                                                          dict.get(DictKeyConstant.COMMANDS))

# encoding: utf-8
# !/usr/bin/python3
from pi_client.cache.PiClientCache import tcpServiceChannelMapCache
from pi_common.communication.tcp.client.TcpSocketClientMagSend import TcpSocketClientMagSend
from pi_drive.handle.algorithm.L298N.L298NAlgorithm import L298NAlgorithm
from pi_common.constant.Constant import *
import threading, time
from pi_common.util.structure.Map import Map
from pi_client.web.web_service.models.CarMove import CarMove
from pi_client.core.handle.ParameterSynchronizationTask import ParameterSynchronizationTask
from pi_client.cache.ClientCoreCache import parameterSynchronizationTaskQueue
from pi_common.constant.DictKeyConstant import DictKeyConstant
from pi_drive.cache.DriveCache import directiveParameterMap,modularToTaskId\
    ,taskIdTotriggerTaskMap, directiveCommadAlgorithmLoadType

carUserMap = Map()

"""
小车控制
"""


class CarControl:
    """移动"""

    @staticmethod
    def move(yl_, yr_, ruler_yl_, ruler_yr_, addresss_, username_):
        # carMove = carUserMap.get(username_)
        # if carMove is None:
        #     carMove = CarMove()
        #     carMove.caerteTime = time.time()
        #     carMove.addresss = addresss_
        # if yl_ is not '': carMove.yl = float(yl_)
        # if yr_ is not '': carMove.yr = float(yr_)
        # if ruler_yl_ is not '': carMove.ruler_yl = float(ruler_yl_)
        # if ruler_yr_ is not '': carMove.ruler_yr = float(ruler_yr_)
        # carMove.updateTime = time.time()
        # carUserMap.put(username_, carMove)

        if directiveCommadAlgorithmLoadType.get(
                'L298N' + DictKeyConstant.CLIENT_SUFFIX) is True:  # 同步
            parameters = {}
            parameters['yl'] = yl_
            parameters['yr'] = yr_
            parameters['ruler_yl'] = ruler_yl_
            parameters['ruler_yr'] = ruler_yr_
            dict[DictKeyConstant.MODULAR_IDENTIFICATION] = 'L298N_1'
            task = ParameterSynchronizationTask()
            task.key = 'L298N_1'
            task.value = parameters
            task.addresss = addresss_
            parameterSynchronizationTaskQueue.add(task)
        else:
            dict = directiveParameterMap.get('L298N_1')
            dict[DictKeyConstant.MODULAR_IDENTIFICATION] = 'L298N_1'
            dict['yl'] = yl_
            dict['yr'] = yr_
            dict['ruler_yl'] = ruler_yl_
            dict['ruler_yr'] = ruler_yr_
            dict['addresss'] = addresss_
            taskId = modularToTaskId.get('L298N_1')
            externalTriggerTask = taskIdTotriggerTaskMap.get(taskId)
            externalTriggerTask.execute(dict)

        # print('updat: yl' + str(carMove.yl) + 'yr' + str(carMove.yr))

    """停止"""

    @staticmethod
    def stop():
        pass


class CarCommandThread(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        while True:
            if not carUserMap.isEmpty():
                newTime = time.time()
                for key in list(carUserMap.keys()):
                    carMove = carUserMap.get(key)
                    if newTime - carMove.caerteTime > CAR_INACTIVATION_TIME:
                        carUserMap.removeChannel(key)
                    elif carMove.yl != 0.0 or carMove.yr != 0.0:
                        try:
                            print(
                                '\033[5;35;2m%s\033[0m' % ('CarCommand yl' + str(carMove.yl) + 'yr' + str(carMove.yr)))
                            dict = carMove.toDict()

                            commands = L298NAlgorithm.buildDirectiveCommand(dict)
                            for address in carMove.addresss:
                                tcpChannelCacheEntity = tcpServiceChannelMapCache.get(address.strip())
                                if tcpChannelCacheEntity != None:
                                    TcpSocketClientMagSend.sendMsgCommand(tcpChannelCacheEntity.tcpSocketClient.channel,
                                                                          commands)
                        except Exception as e:
                            print("car 驱动命令无法构建或发送" + e)

            time.sleep(CAE_MOVE_DRIVING_TIME)

# carCommandThread = CarCommandThread("carCommandThread")
# carCommandThread.start()

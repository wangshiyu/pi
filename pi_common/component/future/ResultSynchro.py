# encoding: utf-8
# !/usr/bin/python3

from pi_common.util.structure.Map import Map
from threading import Condition, Thread
from pi_common.component.future.RequestSynchroData import RequestSynchroData
from pi_common.exception.PiException import TimeOutException
import time
from pi_common.communication.tcp.client.TcpSocketClientMagSend import TcpSocketClientMagSend

"""
结果同步返回
"""


class ResultSynchro(Thread):
    resultReturnCacheMap = Map()  # 存放返回结果
    thisCond = Condition()  # 多线程条件

    ### 请求对应地址
    def request(self, msgId, address, channel, requestDate, timeOut=100):
        cond = Condition()  # 多线程条件
        requestSynchroData = RequestSynchroData()
        requestSynchroData.cond = cond
        requestSynchroData.id = msgId
        requestSynchroData.address = address
        requestSynchroData.channel = channel
        requestSynchroData.requestDate = requestDate
        # requestSynchroData.threadInstance = threadInstance
        requestSynchroData.timeOut = timeOut
        self.resultReturnCacheMap.put(msgId, requestSynchroData)
        with self.thisCond:
            print("notify this.....")
            self.thisCond.notify()
        TcpSocketClientMagSend.sendMsg(channel, requestDate)  # 发送消息
        with cond:
            print("ResultSynchro wait.....")
            cond.wait()

        if requestSynchroData.timeOutSign: TimeOutException(
            "connect address:" + address + " TimeOutException time is:" + str(timeOut) + "ms")
        self.resultReturnCacheMap.removeChannel(msgId)
        return requestSynchroData.resultDate

    ### set返回结果
    def setResponse(self, msgId, responseDate):
        requestSynchroData = self.resultReturnCacheMap.get(msgId)
        if requestSynchroData is not None:
            requestSynchroData.responseDate = responseDate
            with requestSynchroData.cond:
                print("notify .....")
                requestSynchroData.cond.notify()

    # 清理缓存队列
    def run(self):
        with self.thisCond:
            print("wait this.....")
            self.thisCond.wait()
        nowTime = int(round(time.time() * 1000))
        keys = self.resultReturnCacheMap.keys
        for key in keys:
            requestSynchroData = self.resultReturnCacheMap.get(key)
            if requestSynchroData.createTime + requestSynchroData.timeOut > nowTime and requestSynchroData.responseDate is None:
                requestSynchroData.timeOutSign = True
                with requestSynchroData.cond:
                    print("notify .....")
                    requestSynchroData.cond.notify()
                    self.resultReturnCacheMap.removeChannel(key)


if __name__ == '__main__':
    resultSynchro = ResultSynchro()
    resultSynchro.start()

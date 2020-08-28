# encoding: utf-8
# !/usr/bin/python3
from pi_drive.task.BaseTriggerTask import BaseTriggerTask
from apscheduler.schedulers.blocking import BlockingScheduler
from pi_common.constant.DictKeyConstant import DictKeyConstant
from pi_common.util.ReflexUtil import ReflexUtil

"""
毫秒触发任务
"""


class MsecTriggerTask(BaseTriggerTask):
    sched = None

    def __init__(self):
        self.sched = BlockingScheduler()

    def addTask(self, dict):
        parameters = dict.get(DictKeyConstant.TRIGGER_TASK_PARAMETERS)
        taskId = dict.get(DictKeyConstant.TRIGGER_TASK_ID)
        return self.sched.add_job(self.execute, trigger='interval', args=(dict,), id=taskId, seconds=parameters[0])

    def removeTask(self, dict):
        task = dict.get(DictKeyConstant.TASK)
        self.sched.remove_job(task.id)

    def execute(self, dict):
        print("执行任务")
        super().execute(dict)

    def start(self):
        self.sched.start()

    def close(self):
        self.sched.shutdown()
        self.sched = None


# if __name__ == '__main__':
#     # sched = BlockingScheduler()
#     # sched.add_job(newOrder, 'interval', args=(1,), seconds=1)
#     # sched.add_job(newOrder, 'interval', args=(2,), seconds=0.2)
#     # sched.start()
#     #msecTriggerTask = MsecTriggerTask()
#     msecTriggerTask = ReflexUtil.modelGetExample("pi_drive.task.MsecTriggerTask","MsecTriggerTask")
#     dict = {}
#     dict[DictKeyConstant.TRIGGER_TASK_PARAMETERS]=[5]
#     dict['taskId']= 'carLeft1'
#     dict['str'] = '111'
#     msecTriggerTask.addTask(dict)
#     msecTriggerTask.start()
#     dict = {}
#     dict[DictKeyConstant.TRIGGER_TASK_PARAMETERS]=[5]
#     dict['taskId']= 'carLeft2'
#     dict['str'] = '222'
#     msecTriggerTask.addTask(dict)
#     msecTriggerTask.start()
# encoding: utf-8
# !/usr/bin/python3
from pi_drive.task.BaseTriggerTask import BaseTriggerTask
from apscheduler.schedulers.blocking import BlockingScheduler
from pi_common.constant.DictKeyConstant import DictKeyConstant
import datetime

"""
一次性触发任务
"""
class OneTriggerTask(BaseTriggerTask):

    sched = None

    def __init__(self):
        self.sched = BlockingScheduler()

    def addTask(self, dict):
        parameters = dict.get(DictKeyConstant.TRIGGER_TASK_PARAMETERS)
        taskId = dict.get(DictKeyConstant.TRIGGER_TASK_ID)
        return self.sched.add_job(self.execute, 'corn', args=(dict,), id=taskId, next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=parameters[0]))

    def removeTask(self, dict):
        task = dict.get(DictKeyConstant.TASK)
        self.sched.remove_job(task.id)

    def execute(self, dict):
        super().execute(dict)

    def start(self):
        self.sched.start()

    def close(self):
        self.sched.shutdown()
        self.sched = None


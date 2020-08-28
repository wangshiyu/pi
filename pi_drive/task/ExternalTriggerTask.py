# encoding: utf-8
# !/usr/bin/python3
from pi_drive.task.BaseTriggerTask import BaseTriggerTask
from apscheduler.schedulers.blocking import BlockingScheduler
from pi_common.constant.DictKeyConstant import DictKeyConstant

"""
外部触发任务
"""


class ExternalTriggerTask(BaseTriggerTask):
    """
    任务直接执行
    """

    def execute(self, dict):
        print("执行任务")
        super().execute(dict)

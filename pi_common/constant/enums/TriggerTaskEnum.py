# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique
from pi_drive.task.CornTriggerTask import CornTriggerTask
from pi_drive.task.ExternalTriggerTask import ExternalTriggerTask
from pi_drive.task.MsecTriggerTask import MsecTriggerTask
from pi_drive.task.OneTriggerTask import OneTriggerTask

"""
任务触发器实例枚举
"""


class TriggerTaskExampleEnum(Enum):
    CornTriggerTask = CornTriggerTask()
    ExternalTriggerTask = ExternalTriggerTask()
    MsecTriggerTask = MsecTriggerTask()
    OneTriggerTask = OneTriggerTask()

    @staticmethod
    def get(key):
        for enum in TriggerTaskExampleEnum:
            if key in str(enum):
                return enum.value

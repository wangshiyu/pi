# encoding: utf-8
# !/usr/bin/python3
"""
任务队列执行器
"""


class TaskQueueExecute:
    dict = None

    def __init__(self, dict=None):
        self.dict = dict

    def execute(self, task):
        print("task execute")

# encoding: utf-8
# !/usr/bin/python3
"""
FuturesThreadPool 任务
"""


class FuturesTask:
    dict = None

    def __init__(self, dict):
        self.dict = dict

    def execute(self, dict):
        print(dict)

# encoding: utf-8
# !/usr/bin/python3
"""
指令选择器
"""
import abc


class ExecuteSelector(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def addMsg(msg, address_str):
        pass

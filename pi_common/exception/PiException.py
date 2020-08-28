# encoding: utf-8
# !/usr/bin/python3


# 通过继承Exception或者BaseException类实现自定义异常类
class NullException(BaseException):
    def __init__(self, mesg="raise a NullException"):
        print(mesg)

# 通过继承Exception或者BaseException类实现自定义异常类
class NotConfiguredException(BaseException):
    def __init__(self, mesg="raise a NotConfiguredException"):
        print(mesg)

# 通过继承Exception或者BaseException类实现自定义异常类
class TimeOutException(BaseException):
    def __init__(self, mesg="raise a TimeOutException"):
        print(mesg)
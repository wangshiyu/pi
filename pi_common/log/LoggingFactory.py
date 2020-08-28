# encoding: utf-8
# !/usr/bin/python
import logging
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

"""
工程使用需求：
1-不同日志名称
2-打印同时在控制台，也有文件
3-录活控制等级
"""


# logging.disable(logging.CRITICAL)   # 禁止输出日志
class LoggingFactory(object):

    def __init__(self):
        pass

    def public_log(self,logger_name='default-log', log_file=os.path.join(BASE_DIR, 'log', 'dataoperate.log'),
                     level=logging.INFO):
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)  # 添加日志等级
        # 创建控制台 console handler
        ch = logging.StreamHandler()
        # 设置控制台输出时的日志等级
        ch.setLevel(logging.DEBUG)
        # 创建文件 handler
        fh = logging.FileHandler(filename=log_file, encoding='utf-8')
        # 设置写入文件的日志等级
        fh.setLevel(logging.DEBUG)
        # 创建文件 PI handler
        ph = PiHandler()
        ph.setLevel(logging.INFO)
        # 创建 formatter
        formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s')
        # 添加formatter
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        ph.setFormatter(formatter)
        # 把ch fh 添加到logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        logger.addHandler(ph)
        return logger


"""
pi 日志处理器
"""


class PiHandler(logging.Handler):
    terminator = '\n'

    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        try:
            msg = self.format(record)
            if queueOpen:
               if len(queue)>=queueMaxLen:
                  queue.pop(0)
               queue.append(msg)

        except Exception:
            self.handleError(record)


logger = LoggingFactory().public_log()
queueOpen = False
queueMaxLen =100
queue = list()
def setQueueOpen(falg):
    global queueOpen
    queueOpen=falg

def setQueueMaxLen(maxLen):
    global queueMaxLen
    queueMaxLen=maxLen


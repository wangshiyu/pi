# encoding: utf-8
# !/usr/bin/python3
import time
import queue
import threading
from threading import Condition

"""
通用任务队列
"""


# 条件变量

class TaskQueue:
    cond = None # 多线程条件
    queueName = None  # 队列名称
    queue = None  # 队列
    createTime = None  # 创建时间
    updateTime = None  # 更新时间
    taskQueueThread = None  # 线程消耗队列
    previousTask = None  # 上条执行的任务
    taskQueueExecute = None  # 执行器

    def __init__(self, queueName, taskQueueExecute):
        self.cond = Condition()
        self.queue = queue.Queue()
        self.createTime = time.time()
        self.updateTime = time.time()
        self.queueName = queueName
        self.taskQueueExecute = taskQueueExecute
        self.taskQueueThread = TaskQueueThread(self)
        self.taskQueueThread.start()

    def add(self, task):
        self.queue.put(task)
        self.updateTime = time.time()
        with self.cond:
            self.cond.notify()
            print("notify.....")

    def clear(self):
        self.queue.clear()  # 清空队列
        return self.previousTask

    def close(self):
        pass


class TaskQueueThread(threading.Thread):
    close = False
    __taskQueue = None

    def __init__(self, taskQueue):
        threading.Thread.__init__(self)
        self.__taskQueue = taskQueue

    def run(self):
        while not self.close:
            if self.__taskQueue.queue.empty():
                with self.__taskQueue.cond:
                    print("TaskQueue wait.....")
                    self.__taskQueue.cond.wait()
            else:
                task = self.__taskQueue.queue.get()
                self.__taskQueue.previousTask = task
                try:
                    self.__taskQueue.taskQueueExecute.execute(task)
                except Exception as e:
                    print("Exception",e)


if __name__ == '__main__':
    from pi_common.component.task_queue.TaskQueueExecute import TaskQueueExecute
    from pi_common.component.task_queue.Task import Task

    taskQueueDate = TaskQueue("test", TaskQueueExecute())
    while True:
        taskQueueDate.add(Task())

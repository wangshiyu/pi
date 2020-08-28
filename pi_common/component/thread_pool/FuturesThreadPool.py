# encoding: utf-8
# !/usr/bin/python3


from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED, wait

"""
Futures 线程池
"""


class FuturesThreadPool:
    executor = None

    def __init__(self, maxWorkers):
        self.executor = ThreadPoolExecutor(max_workers=maxWorkers)

    def submitTask(self, task):
        return self.executor.submit(task.execute, task.dict)

    def submitTaskResult(self, task):
        task_ = self.executor.submit(task.execute, task.dict)
        return task_.result()

    def submitTasks(self, tasks):
        all_task = [self.executor.submit(task.execute, task.dict) for task in tasks]
        wait(all_task, return_when=ALL_COMPLETED) # 所有任务执行完

# done方法用于判定某个任务是否完成
# print(task1.done())
# cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
# print(task1.cancel())
# 返回结果
# print(task1.result())


# from pi_common.component.thread_pool.FuturesTask import FuturesTask
# futuresThreadPool = FuturesThreadPool(2)
# task = FuturesTask({})
# #task.execute({})
# task.dict['wsy'] = 111
# print(futuresThreadPool.submitTask(task))

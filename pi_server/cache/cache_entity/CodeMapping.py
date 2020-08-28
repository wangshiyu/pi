# encoding: utf-8
# !/usr/bin/python3
import time

"""
代码映射缓存实体
"""


class CodeMapping:
    directiveCommandCode = None  # 驱驱动指令 对应的别名
    createTime = time.time()  # 建立时间
    invokingTime = time.time()  # 上次调用时间
    invokingSize = 0
    codeStr = None  # 代码

    def __init__(self, directiveCommandCode, codeStr):
        self.directiveCommandCode = directiveCommandCode
        self.codeStr = codeStr

# encoding: utf-8
# !/usr/bin/python3

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""
服务端启动
"""
from pi_server.core.ServerCore import ServerCore
from pi_common.log.LoggingFactory import setQueueOpen


if __name__ == "__main__":
    import pi_server.cache.ServerCoreCache
    # 加载下面模块
    import pi_drive.load.TriggerInfoLoad
    import pi_drive.load.DirectiveCommadAlgorithmLoad
    import pi_drive.load.DirectiveHardwareLoad
    setQueueOpen(True)
    ServerCore().init()
# encoding: utf-8
# !/usr/bin/python3

"""
客户端启动
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pi_client.cache.ClientCoreCache import clientCore
from pi_client.web.django.manage import web_init

if __name__ == '__main__':
    # 加载下面模块
    import pi_common.config.Config
    import pi_drive.load.TriggerInfoLoad
    import pi_drive.load.DirectiveCommadAlgorithmLoad
    import pi_drive.load.DirectiveHardwareLoad
    import pi_drive.load.ParametersMappingLoad
    clientCore.init()
    web_init()

# encoding: utf-8
# !/usr/bin/python3
from pi_common.util.structure import Map
import sys
from enum import Enum, unique
from pi_common.util.PropertiesUtiil import Properties

"""
用于Config配置
"""
configMapCache = Map.Map()

confJson = Properties("../conf.properties").getProperties()

class ConfigEnum(Enum):
    PATTERN = 'pattern'  # 启动模式 test ,run
    ADDRESS = 'address'  # 地址
    START = 'start'  # 启动类
    RUN_TYPE = 'runTypr'  # 启动类型 server ，client


class ConfigValueEnum(Enum):
    server = 'server'
    client = 'client'
    all = 'all'
    unknown = 'unknown'
    test = 'test'
    run = 'run'


configMapCache.put(ConfigEnum.START._value_, sys.argv[0]);


def confJsonHandle(json):
    for configEnum in ConfigEnum:
        for key in json.keys():
            if configEnum._value_ in key:
                configMapCache.put(key, json.get(key))


if 'StartServer.py' in sys.argv[0]:
    serverJson = confJson.get(ConfigValueEnum.server.value)
    confJsonHandle(serverJson)
    configMapCache.put(ConfigEnum.RUN_TYPE._value_, ConfigValueEnum.server._value_)
elif 'StartClient.py' in sys.argv[0]:
    clientJson = confJson.get(ConfigValueEnum.client.value)
    confJsonHandle(clientJson)
    configMapCache.put(ConfigEnum.RUN_TYPE._value_, ConfigValueEnum.client._value_)
else:
    configMapCache.put(ConfigEnum.RUN_TYPE._value_, ConfigValueEnum.unknown._value_)

# for key in ConfigEnum:
#     for parameter in sys.argv:
#         if key._value_ in parameter:
#             if '=' in parameter:
#                 configMapCache.put(key._value_, parameter.split('=')[1])
#                 if configMapCache.get(ConfigEnum.RUN_TYPE._value_) == ConfigValueEnum.client._value_:
#                     sys.argv.remove(parameter)


"""
Config 配置类
"""


class Config:

    @staticmethod
    def getConfig(key):
        return configMapCache.get(key._value_)

    @staticmethod
    def existence(key, value):
        if configMapCache.get(key._value_) is None:
            return False
        else:
            if value in configMapCache.get(key._value_):
                return True
            else:
                return False

    @staticmethod
    def eq(key, configValueEnum):
        if configMapCache.get(key._value_) is None:
            return False
        else:
            if configValueEnum.value == configMapCache.get(key._value_):
                return True
            else:
                return False

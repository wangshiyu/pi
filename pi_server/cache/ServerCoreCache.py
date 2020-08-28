# encoding: utf-8
# !/usr/bin/python3
from pi_common.config.Config import Config,ConfigValueEnum, ConfigEnum
from pi_server.core.external_handle.ServerTriggerTaskCommandHandle import ServerTriggerTaskCommandHandle
from pi_drive.cache.DriveCache import *

if Config.eq(ConfigEnum.RUN_TYPE,ConfigValueEnum.server):
    setTriggerTaskCommandHandle(ServerTriggerTaskCommandHandle())
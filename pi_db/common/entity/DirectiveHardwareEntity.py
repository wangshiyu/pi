# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String, Time
from pi_db.common.entity.BaseEntity import BaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
DirectiveHardwareEntity对象
# 驱动硬件映射表
"""


class DirectiveHardwareEntity(DeclarativeBase, BaseEntity):
    # 表的名字:
    __tablename__ = 'tb_directive_hardware'
    # 表的结构:
    directiveIdentification = Column(String, name='directive_identification')  # 驱动标记
    hardwareIdentification = Column(String, name='hardware_identification')  # 硬件标记
    modularIdentification = Column(String(40), name='modular_identification')  #（驱动和硬件）模块标记
    channelJson = Column(String, name='channel_json')  #  信道参数json
    calculation = Column(String(40), name='calculation')  # 计算 server,client
    executeJson = Column(String, name='execute_json')  # 执行json
    directiveCommadAlgorithmJson = Column(String, name='directive_commad_algorithm_json')  # 驱动命令算法Json
    triggerTaskId = Column(String(40), name='trigger_task_id')  # 触发器id
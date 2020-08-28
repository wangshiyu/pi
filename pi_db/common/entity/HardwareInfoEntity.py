# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String, Time
from pi_db.common.entity.BaseEntity import BaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
HardwareInfoEntity对象
# 硬件信息表
"""


class HardwareInfoEntity(DeclarativeBase, BaseEntity):
    # 表的名字:
    __tablename__ = 'tb_hardware_info'
    # 表的结构:
    identification = Column(String(40))  # 标记
    name = Column(String(40))  # 驱动模块
    info = Column(String)  # 详情


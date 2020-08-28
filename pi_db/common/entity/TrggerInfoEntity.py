# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String, Time
from pi_db.common.entity.BaseEntity import BaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
TrggerInfoEntity对象
# 触发器
"""


class TrggerInfoEntity(DeclarativeBase, BaseEntity):
    # 表的名字:
    __tablename__ = 'tb_trgger_info'
    # 表的结构:
    loadType = Column(String(40), name='load_type')  # 加载类型
    triggerTaskId = Column(String(40), name='trigger_task_id')  # 触发器id 全局唯一
    triggerTaskJson = Column(String, name='trigger_task_json')  # 触发器配置
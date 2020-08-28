# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String, Time
from pi_db.common.entity.BaseEntity import BaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
DirectiveInfoEntity对象
# 驱动配置信息表
"""


class DirectiveInfoEntity(DeclarativeBase, BaseEntity):
    # 表的名字:
    __tablename__ = 'tb_directive_info'
    # 表的结构:
    userId = Column(Integer, name='user_id')  # 用户id
    directiveName = Column(String(40), name='directive_name')  # 驱动名称
    modularName = Column(String, name='modular_name')  # 模块名称
    className = Column(String, name='class_name')  # 类名称
    methodJson = Column(String, name='method_json')  # 方法
    importCodeJson = Column(String, name='import_code_json')  # 导入code
    initCode = Column(String, name='init_code')  # 初始化code
    otherCode = Column(String, name='other_code')  # 其他code
    pattern = Column(String(10), name='pattern')  # 驱动模式
    identification = Column(String(40))  # 标记


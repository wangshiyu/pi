# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String, Time
from pi_db.common.entity.BaseEntity import BaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
DirectiveCommadAlgorithm对象
#   驱动命令算法表
"""


class DirectiveCommadAlgorithmEntity(DeclarativeBase, BaseEntity):
    # 表的名字:
    __tablename__ = 'tb_directive_commad_algorithm'
    # 表的结构:

    algorithmSign = Column(String(40), name='algorithm_sign')  # 算法标记
    commandHandle = Column(String, name='command_handle')  # 对应算法
    handleModel = Column(String, name='handle_model')  # 对应算法模块
    inputParameterTypeJson = Column(String, name='input_parameter_type_json')  # 算法输入参数
    name = Column(String(40), name='name')  # 算法名称
    info = Column(String)  # 详情
    loadType = Column(Integer, name='load_type')  # 加载类型 1服务端 2客户端
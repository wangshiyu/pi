# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String, Time
from pi_db.common.entity.BaseEntity import BaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
DirectiveRequestParameterMappingEntity
# 驱动请求参数映射表
"""


class DirectiveRequestParameterMappingEntity(DeclarativeBase, BaseEntity):
    # 表的名字:
    __tablename__ = 'tb_directive_request_parameter_mapping'
    # 表的结构:
    modularIdentification = Column(String(40), name='modular_identification')  #（驱动和硬件）模块标记
    algorithmSign = Column(String(40), name='algorithm_sign')  #算法标记
    parametersMappingJson = Column(String, name='parameters_mapping_json')  # 参数映射json

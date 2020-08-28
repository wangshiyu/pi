# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String
from pi_db.client.entity.ClientBaseEntity import ClientBaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
ManipulateComponenEntity对象
# 操控组件表
"""


class ManipulateComponenEntity(DeclarativeBase, ClientBaseEntity):
    # 表的名字:
    __tablename__ = 'tb_manipulate_componen'
    # 表的结构:
    component = Column(String(12))  # 组件类型
    layerDateJson = Column(String, name='layer_date_json')  # 层数据
    layerStyleJson = Column(String, name='layer_style_json')  # 层样式
    layerJsJson = Column(String, name='layer_js_json')  # 层js

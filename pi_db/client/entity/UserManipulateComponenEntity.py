# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String
from pi_db.client.entity.ClientBaseEntity import ClientBaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
UserManipulateComponenEntity对象
用户操控页面组件表
"""


class UserManipulateComponenEntity(DeclarativeBase, ClientBaseEntity):
    # 表的名字:
    __tablename__ = 'tb_user_manipulate_componen'
    # 表的结构:
    userId = Column(Integer, name='user_id')  # 用户id
    manipulatePageId = Column(Integer, name='manipulate_page_id')  # 用户操控页面id
    componenId = Column(Integer, name='componen_id')  # 组件id
    layerDateJson = Column(String, name='layer_date_json')  # 层数据
    layerStyleJson = Column(String, name='layer_style_json')  # 层样式
    layerJsJson = Column(String, name='layer_js_json')  # 层js
    parametersJson = Column(String, name='parameters_json')  # 参数json

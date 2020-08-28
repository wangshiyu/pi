# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String
from pi_db.client.entity.ClientBaseEntity import ClientBaseEntity
from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base()
"""
UserManipulatePageEntity对象
用户操控界面表
"""


class UserManipulatePageEntity(DeclarativeBase,ClientBaseEntity):
    # 表的名字:
    __tablename__ = 'tb_user_manipulate_page'
    # 表的结构:
    userId = Column(Integer, name='user_id')  # 用户id
    name = Column(String(20))  # 名称
    grade = Column(Integer)  # 排级

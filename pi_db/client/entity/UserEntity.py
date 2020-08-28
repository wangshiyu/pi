# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String
from pi_db.client.entity.ClientBaseEntity import ClientBaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
UserEntity对象
用户表
"""


class UserEntity(DeclarativeBase, ClientBaseEntity):
    # 表的名字:
    __tablename__ = 'tb_user'
    # 表的结构:
    name = Column(String(12))  # 名称
    password = Column(String(32))  # 密码
    privilegeLevel = Column(Integer, name='privilege_level', default=0)  # 权限等级

# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String
from pi_db.client.entity.ClientBaseEntity import ClientBaseEntity
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
"""
UserTcpAddress对象
用户TCP连接地址表
"""


class UserTcpAddressEntity(DeclarativeBase, ClientBaseEntity):
    # 表的名字:
    __tablename__ = 'tb_user_tcp_address'
    # 表的结构:
    userId = Column(Integer, name='user_id')  # 用户id
    address = Column(String(40))  # 地址

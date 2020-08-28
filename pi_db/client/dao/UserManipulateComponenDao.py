# encoding: utf-8
# !/usr/bin/python3
from pi_db.client.dao.ClientBaseDao import ClientBaseDao
from pi_db.client.entity.UserManipulateComponenEntity import UserManipulateComponenEntity

"""
用户操控页面组件Dao
"""


class UserManipulateComponenDao(ClientBaseDao):
    entityClass = UserManipulateComponenEntity





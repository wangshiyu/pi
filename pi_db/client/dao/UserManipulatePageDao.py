# encoding: utf-8
# !/usr/bin/python3
from pi_db.client.dao.ClientBaseDao import ClientBaseDao
from pi_db.client.entity.UserManipulatePageEntity import UserManipulatePageEntity

"""
用户操控页面Dao
"""


class UserManipulatePageDao(ClientBaseDao):
    entityClass = UserManipulatePageEntity
# encoding: utf-8
# !/usr/bin/python3
from pi_db.client.dao.ClientBaseDao import ClientBaseDao
from pi_db.client.entity.ManipulateComponenEntity import ManipulateComponenEntity

"""
操控组件Dao
"""


class ManipulateComponenDao(ClientBaseDao):
    entityClass = ManipulateComponenEntity

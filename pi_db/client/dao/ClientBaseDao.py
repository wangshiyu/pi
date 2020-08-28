# encoding: utf-8
# !/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pi_db.common.dao.BaseDao import BaseDao

basedir = os.path.abspath(os.path.dirname(__file__))
dbConnectStr = 'sqlite:///' + os.path.join(basedir, 'pi_client.db')

# 创建数据库连接
engine = create_engine(dbConnectStr)
# 获取元数据
# metadata = MetaData(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


class ClientBaseDao(BaseDao):
    entityClass = None
    session = DBSession()

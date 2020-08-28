# encoding: utf-8
# !/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
dbConnectStr = 'sqlite:///' + os.path.join(basedir, 'pi_common.db')

# 创建数据库连接
engine = create_engine(dbConnectStr)
# 获取元数据
# metadata = MetaData(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


class BaseDao:
    entityClass = None
    session = DBSession()

    def getById(self, id):
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        entity = self.session.query(self.entityClass).filter(self.entityClass.id == id).one()
        # 关闭Session:
        self.session.close()
        return entity

    def getListByEntity(self, entity):
        result = ExecResult()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        #self.session.query(self.entityClass).filter(self.entityClass.name=='wsy').all()
        code = "list = self.session.query(self.entityClass).filter(" + BaseDao.filterParameter(
            entity) + ").all() \nresult.list=list "
        exec(code)
        # 关闭Session:
        self.session.close()
        return result.list

    def getPageCount(self, entity):
        result = ExecResult()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        #self.session.query(self.entityClass).filter(self.entityClass.name=='wsy')
        code = "list = self.session.query(self.entityClass).filter(" + BaseDao.filterParameter(
            entity) + ").all() \nresult.list=list "
        exec(code)
        # 关闭Session:
        self.session.close()
        return len(result.list)

    def getPageDate(self, entity):
        result = ExecResult()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        #self.session.query(self.entityClass).filter(self.entityClass.name=='wsy').
        code = "list = self.session.query(self.entityClass).filter(" + BaseDao.filterParameter(
            entity) + ").limit(entity.limit).offset(entity.offset).all() \nresult.list=list "
        exec(code)
        # 关闭Session:
        self.session.close()
        return result.list

    def insert(self, entity):
        entity.createTime = datetime.datetime.now()
        # 添加到session:
        result = self.session.add(entity)
        # 提交即保存到数据库:
        self.session.commit()
        # 关闭session:
        self.session.close()
        return result

    def updata(self, entity):
        result = self.session.query(self.entityClass).filter(self.entityClass.id == entity.id).one()
        BaseDao.__copy(result, entity)
        result.updateTime = datetime.datetime.now()
        self.session.commit()
        self.session.close()
        return result

    def delete(self, id):
        result = self.session.query(self.entityClass).filter(self.entityClass.id == id).delete()
        self.session.commit()
        self.session.close()
        return result

    @staticmethod
    def __copy(a, b):
        if b == None: return None;
        attributeList = b.__dict__
        for attribute in attributeList:
            if 'id' == attribute: continue
            if 'metadata' == attribute: continue
            if attribute.find('__') > -1 or attribute.find('_') > -1: continue
            if hasattr(a, attribute):
                setattr(a, attribute, getattr(b, attribute))

    @staticmethod
    def filterParameter(entity):
        if entity == None: return None;
        filterParameter = list()
        for attribute in entity.__dict__:
            if 'metadata' == attribute \
                    or 'offset' == attribute\
                    or 'limit' == attribute: continue
            if attribute.find('__') > -1 or attribute.find('_') > -1: continue
            if getattr(entity, attribute) is not None:
                value = None
                if type(getattr(entity, attribute)) == type('str'):
                    value = '\'' + str(getattr(entity, attribute)) + '\''
                else:
                    value = str(getattr(entity, attribute))
                filterParameter.append('self.entityClass.' + str(attribute) + "==" + value)
        return ','.join(filterParameter)


"""
执行返回实体
"""


class ExecResult:
    list = None

# encoding: utf-8
# !/usr/bin/python3
from pi_db.client.dao.ClientBaseDao import ClientBaseDao
from pi_db.client.entity.UserEntity import UserEntity

"""
用户Dao
"""


class UserDao(ClientBaseDao):
    entityClass = UserEntity

    # def updata(self, entity):
    #     result = self.session.query(self.entityClass).filter(self.entityClass.id == entity.id).one()
    #     result.name = entity.name
    #     self.session.commit()
    #     self.session.close()
    #     return result


if __name__ == '__main__':
    user = UserDao().getById(8)
    print(user.id)
    # user= UserEntity(id=9,name="小米0")
    # attributeList = dir(user)
    # print(attributeList)
    # UserDao().updata(user)
    print(UserDao().delete(8))

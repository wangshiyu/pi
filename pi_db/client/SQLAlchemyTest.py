from sqlalchemy import create_engine, Table, Column, Integer, String, Date, Time, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

basedir = os.path.abspath(os.path.dirname(__file__))
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'tb_user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(12))
    password = Column(String(32))
    createTime = Column(Time, name='create_time')
    privilegeLevel = Column(Integer, name='privilege_level')

dbStr = 'sqlite:///' + os.path.join(basedir, 'pi_client.db')
# 创建数据库连接
engine = create_engine(dbStr)
# 获取元数据
#metadata = MetaData(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

"""数据写入"""

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(name='ww11', password='wsy', createTime=None, privilegeLevel=None)
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()



"""
查询
"""

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='2').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
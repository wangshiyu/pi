import sqlite3

# '''创建一个数据库，文件名'''
conn = sqlite3.connect('./pi_client.db')
# '''创建游标'''
cursor = conn.cursor()

# '''执行语句'''

sql = '''create table students (
        name text,
        username text,
        id int)'''

cursor.execute(sql)

# '''使用游标关闭数据库的链接'''
cursor.close()
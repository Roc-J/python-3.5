# coding:utf-8
import os,sqlite3

db_file=os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)

#初始数据
#连接到SQLite数据库
#数据库文件是test.db
#如果文件不存在，会自动在当前目录创建
conn=sqlite3.connect(db_file)
#创建一个Cursor(游标)
cursor= conn.cursor()
#执行一条SQL语句，创建user表
cursor.execute('create table user(id varchar(20) primary key,name varchar(20),score int)')
#执行三条SQL语句，插入三条记录
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values ('A-002','Bart',62)")
cursor.execute(r"insert into user values ('A-003','Lisa',78)")

#关闭Cursor
cursor.close()
#提交事务
conn.commit()
#关闭连接
conn.close()

#获取分数，从低到高排序
def get_score_in(low,high):
	#返回指定分俗话区间的名字，按分数从低到高排序
	try:
		#连接到SQLite数据库
		conn=sqlite3.connect(db_file)
		#创建一个Cursor(游标)
		cursor=conn.cursor()
		#执行查询语句
		cursor.execute('select name from user where score between ? and ? order by score asc',(low,high))
		#获取查询结果集
		values=cursor.fetchall()
	finally:
		# 关闭cursor(游标)
		cursor.close()
		conn.commit()
		# 关闭连接
		conn.close()

	#返回结果集
	return list(map(lambda x:x[0],values))



#3-2.py
#创建一个空字典
Dictionary = {}
#定义一个函数，功能：向通讯录中增加记录
#phonebook是通讯录，name是姓名，tel是对应电话号码
def add_phonebook(phonebook, name, tel):
    #增添or更新一条记录
    phonebook[name]=tel
    print("添加成功")

#定义一个函数，功能：查询
# phonebook是通讯录，name是要查找的姓名
def find(phonebook, name):
	#如果name在通讯录内，给出对应电话号码
    if name in phonebook:
    	print("姓名",name,"的电话号码是:", phonebook[name])
    #否则，打印提示信息
    else:
    	print("姓名",name,"不在通讯录内")

#向通讯录内增添几个记录，测试增加记录的功能
while True:
	flag = input("向通讯录中添加记录？(Yes or No)\n")
	if flag == "Yes":
		name = input("姓名: ")    #接受输入
		tel = input("电话号码: ")    
		#调用add_phonebook函数，往通讯录中添加内容
		add_phonebook(Dictionary,name,tel)
	else:
		break

while True:
	op = input("要查询通讯录记录么？(Yes or No)\n")
	if op == "Yes":
		#接收用户输入，调用find函数实现查询
		name = input("输入查询姓名：")
		find(Dictionary,name)
	else:
		break

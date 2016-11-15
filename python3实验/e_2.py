#5-2.py
#输入总人数n，开始号码a，每次出局的号码m
n = input("输入总人数：")
a = input("输入开始号码：")
m = input("输入每次开局的号码：")
n = int(n)
a = int(a)
m = int(m)
#生成号码列表
nameList = []
for i in range(1,n+1):
	nameList.append(i)

#定义函数
def func(nameList, startWith, count):
	if sum(nameList)==0:
		return
	num = (startWith + count -2)%len(nameList)
	#输出每次结果，递归调用
	print(nameList.pop(num))
	func(nameList,num+1,count)

#调用函数
func(nameList, a, m)
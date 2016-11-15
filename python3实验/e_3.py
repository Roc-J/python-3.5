#5-3.py
#定义全局变量计数用
global count

#定义函数
def upStairs(i):
	#读取全局变量
	global count
	if i==0 or i==1:
		count = 1
		return count
	if i==2:
		count = 2
		return count
	if i==3:
		count = 4
		return count
	#遍历3种情况
	count = upStairs(i-1)+upStairs(i-2)+upStairs(i-3)
	return count

#主程序
if __name__ == '__main__':
	n = int(input("How many steps:"))
	count = 0
	upStairs(n)
	print("There are", count, "solutions.")
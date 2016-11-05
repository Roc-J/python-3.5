#3-3.py

#本练习要求：输入一个字符串，统计其中数字、大写字母、小写字母和其他字符出现
#的次数。

#输入一个字符串
string = input("输入一个字符串： \n")
i=0  #变量赋初值
num=0
capital=0
small=0
other=0 
#开启循环
#字符串中每个字符进行操作
while len(string)!=i: 
	#判断是否是数字
	if string[i]>='0' and string[i]<='9':
		num+=1
    #判断是否是大写字母
	elif string[i]>='A' and string[i]<='Z':
		capital+=1
	#判断是否是小写字母
	elif string[i]>='a' and string[i]<='z':
		small+=1
	else:
		other+=1
	i += 1  #循环变量增1

#结果输出
print("该句子中有%d个数字，%d个大写字母，%d个小写字母和%d个其他字符" %(num,capital,small,other))
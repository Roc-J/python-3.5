oplist=[]
while(1):
	op1 = input("请输入一个正数:")
	op1 = int(op1)
	if op1<0:
		print("输入错误!")
		continue
	if op1==0:
		break
	else:
		oplist.append(op1)
oplist.sort(reverse=True)
strlist=""
for x in oplist:
	strlist+=str(x)+" "
print("按成绩从高到低排序后结果为:")
print(strlist)

score = []
while(1):
	name = input("请输入一个姓名:")
	name = str(name)
	if name=="":
		break
	total = input("请输入一个总成绩:")
	math = input("请输入一个数学成绩:")
	
	total = int(total)
	math = int(math)
	item = []
	item.append(name)
	item.append(total)
	item.append(math)
	score.append(item)

score.sort(key=lambda m:[m[1],m[2]],reverse=True)
strresult=""
for x in score:
	strresult+=str(x[0])+" "
print(strresult)

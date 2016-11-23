a = []
scores = []
level = input("请输入层数:")
level = int(level)

for x in range(0,level):
	print("j=",x)
	print("a=",a)
	print("scores=",scores)
	item = []
	itemscore = []
	a.append(item)
	scores.append(itemscore)
	for y in range(0,level-x):
		number = input("请输入第"+str(x)+"层第"+str(y)+"个位置金币数:")
		number = int(number)
		a[x].append(number)
		scores[x].append(0)
		print("输入后a:",a)
		print("输入后scores:",scores)
		print("------------------------")

for i in range(0,level):
	scores[0][i] = a[0][i]
for x in range(1,level):
	for y in range(0,level-x):
		scores[x][y] = max(scores[x-1][y],scores[x-1][y+1])+a[x][y]
		print("i="+str(x)+",j="+str(y)+",走到第i层第j个位置时的最大金币数scores[i][j]：",scores[x][y])
print("------------------")
print("各层scores：",scores)
print("可以获得的金币数量最大是",scores[level-1][0])
#5-1.py
#不需要输入
# 求亲和数
# 如果两个正整数a和b满足：a的所有除本身以外的因数之和等于b，b的所有除本身以外的因数之和等于a，则称a，b是一对亲和数。
# 现请你编一个程序找出所有由两个四位数组成的亲和数对。
affinity = []
#x代表枚举的所有四位数
for x in range(1000,10000):
	#枚举x的所有真因数，并求和
	sum = 0
	for y in range(1,x):
		if x%y == 0:
			sum +=y
	affinity.append(sum)

for i in range(1,9000):
	if affinity[i] >=1000 and affinity[i]<=9999 and affinity[affinity[i]-1000]==(i+1000) and (i+1000)!=affinity[i]:
		print(i+1000,affinity[i])
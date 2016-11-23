import math

def bsearch(listdemo,start,end,x):
	if start>end:
		print("NO FOUND!")
	elif start==end:
		mid = start
	elif start<end:
		mid = int(math.ceil((start+end)/2))

	if listdemo[mid]==x:
		print("在整数序列中的位置编号",mid)
	elif listdemo[mid]>x:
		end = mid-1
		bsearch(listdemo,start,end,x)
	else:
		start = mid+1
		bsearch(listdemo,start,end,x)
	
if __name__ == '__main__':
	listdemo = [1,2,3,4,5,6,7,8,9,10]
	number = input("请输入一个数:")
	number = int(number)
	try:
		bsearch(listdemo,0,len(listdemo)-1,number)
	except Exception as e:
		pass
	
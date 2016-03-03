#python3爬虫教程
#一个简单的实例爬虫
#爬取网站上的图片
#author ：qjk

import urllib.request
import socket
import re
import sys
import os

targerDir = r"E:\learnpython\load" #文件保存路径

def destFile(path):
	if not os.path.isdir(targerDir):
		os.mkdir(targerDir)
	pos = path.rindex('/')
	t = os.path.join(targerDir, path[pos+1:])
	return t

if __name__=="__main__":  #程序运行入口
	weburl = "http://www.douban.com/"
	webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
	req = urllib.request.Request(url=weburl,headers=webheaders) #构造请求报头
	webPage = urllib.request.urlopen(req)
	contentBytes = webPage.read()
	for link ,t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif))',str(contentBytes))):
		print(link)
		try:
			urllib.request.urlretrieve(link, destFile(link)) #下载图片
		except :
			print('失败')
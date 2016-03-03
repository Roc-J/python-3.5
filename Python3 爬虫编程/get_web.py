#python3爬虫教程
#一个简单的实例爬虫
#author ：qjk

import urllib.request
#url = "http://www.douban.com/"
url ='https://www.itjuzi.com/user/login'
webPage = urllib.request.urlopen(url)
data = webPage.read()
print(data)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())

#python3 爬虫教程
#一个简单的实例爬虫
#保存爬取的报文
#author ：qjk

import urllib.request

def saveFile(data):
	save_path= 'E:/learnpython\\temp.out'
	f_obj = open(save_path, 'wb')
	f_obj.write(data)
	f_obj.close()

weburl = "http://www.douban.com/"
webheader1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
webheader2 = {  
    'Connection': 'Keep-Alive',  
    'Accept': 'text/html, application/xhtml+xml, */*',  
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',  
    #'Accept-Encoding': 'gzip, deflate',  
    'Host': 'www.douban.com',  
    'DNT': '1'  
    }  
req = urllib.request.Request(url=weburl, headers=webheader2) 
#req = urllib.request.Request(url=weburl, headers=webheader)
webPage = urllib.request.urlopen(req)
data = webPage.read()
saveFile(data)
data = data.decode('utf-8')
print(data)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())

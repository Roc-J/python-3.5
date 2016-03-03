import urllib.request
import http.cookiejar

username = '15652912457@163.com'
password = '#123456'
#登录的网址
login_url = 'https://www.itjuzi.com/user/login'
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = http.cookiejar.CookieJar()
pro = urllib.request.HTTPCookieProcessor(cj)
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}


#构造登录账户和口令的请求
login_post_dic = {'identity':username, 'password':password}
login_post_data = urllib.parse.urlencode(login_post_dic).encode()

req = urllib.request.Request(login_url, login_post_data, header)
opener = urllib.request.build_opener(pro)  
urllib.request.install_opener(opener) 

op = opener.open(req)
login_result_page = op.read()
print('ok!')

url = 'http://www.itjuzi.com/company/32846'
content = urllib.request.urlopen(url).read()
print(content)



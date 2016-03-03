#!/usr/bin/env python
#coding=utf-8
import sys
import http.cookiejar
import http

try:
    m_host = "https://www.itjuzi.com/user/login"
    m_user = "15652912457@163.com"
    m_passwd = "#211qin381"
    data="username=%s&pwd=%s&Submit=" % (m_user,m_passwd)
   
    #Get的发送头
    Getheaders={"Host":m_host,"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.20) Gecko/20081217 (FoxPlus) Firefox/2.0.0.20","Content-Type":"application/x-www-form-urlencoded"}
   
    #Post的发送头
    Postheaders={"Host":m_host,"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.20) Gecko/20081217 (FoxPlus) Firefox/2.0.0.20","Content-Length":str(len(data)),"Content-Type":"application/x-www-form-urlencoded"}
   
    #连接服务器
    conn=http.client.HTTPSConnection(m_host)
    conn.connect()   
   
    #获取登陆页
    conn.request("GET","",None,Getheaders)
    res=conn.getresponse()
    print (res.read().decode("gbk"))
    print ("/n/n---------------------------------------------------/n/n")
    #Get first over
    #登录
    conn.request("POST","",data,Postheaders)
    #获取cookie:
    resp=conn.getresponse()
    #print (resp.read().decode("gbk"))                      #输出登录结果，有时候会为空或者为报错信息或者为登录页面
    m_cookie = resp.getheader("Set-Cookie").split('_')[0]
   
    Infoheader={"Host":m_host,"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.20) Gecko/20081217 (FoxPlus) Firefox/2.0.0.20","Cookie":m_cookie,"Content-Type":"application/x-www-form-urlencoded"}
   
    #post over
   
    #登录后，访问其它页面
    conn=http.client.HTTPSConnection(m_host)
    conn.request("GET","",None,Infoheader)
    res2=conn.getresponse()
    print (res2.read().decode("gbk"))
except http.client.HTTPException as ex :
     print("value exception occurred ", ex)
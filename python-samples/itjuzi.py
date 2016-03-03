#!/usr/bin/python
#coding=utf-8

import getopt, sys, os, time, datetime
import urllib, re
from urllib import request
from random import randint
import http.cookiejar
#import export

startup_count = 0
body = []

def main():
    try: 
        print(sys.argv)
        login_itjuzi()
        target_url = sys.argv[1]
        page_number_begin = int(sys.argv[2])
        page_number_end = int(sys.argv[3])
        excel_name = sys.argv[4]

        page_number = page_number_begin
        while page_number <= page_number_end:
            crawl_list_page(target_url + str(page_number))
            page_number += 1
        print("startup_count: ", startup_count)

        #export.save_excel(excel_name, extract_head(), body)
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err)) # will print something like "option -a not recognized"
        sys.exit(2)

def login_itjuzi():
    # 账号相关参数
    username = sys.argv[5]
    password = sys.argv[6]
     
    # 测试能否打开https
    #loginUrl = 'https://www.itjuzi.com/user/login'
    #print urllib2.urlopen(loginUrl).read()

    login_url = 'https://www.itjuzi.com/user/login'

    # 保存cookie
    #cookie = cookielib.CookieJar()
    cookie = http.cookiejar.CookieJar()
    #cookie_handler = urllib2.HTTPCookieProcessor(cookie)
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}

    # 构造登录账号和口令的请求
    login_post_dic = {'identity':username, 'password':password, 'Submit':'True'}
    #login_post_data = urllib.urlencode(login_post_dic)
    login_post_data = urllib.parse.urlencode(login_post_dic)

    #req = urllib2.Request(login_url, login_post_data, header)
    req = urllib.request.Request(login_url, login_post_data, header)
    #opener = urllib2.build_opener(cookie_handler)
    #urllib2.install_opener(opener)
    #opener = urllib.build_opener(cookie_handler)
    #urllib.install_opener(opener)
    opener = urllib.request.build_opener(cookie_handler)
    urllib.request.install_opener(opener)

    response = opener.open(req)
    #response = opener.open(login_url, login_post_data)
    login_result_page = response.read()

    # 确认登录成功
    random_sleep();
    test_url = 'https://www.itjuzi.com/user/edit/basic'
    after_login_page = urllib.request.urlopen(test_url).read()
    p_username = re.compile('''<input type="text" name="username" value="(.*?)" class="width-l"  />''', re.IGNORECASE|re.DOTALL);
    username_from_page = p_username.search(after_login_page)
    if username_from_page is not None:
        print("################## login: ", username_from_page.group(1))


def crawl_list_page(list_page_url):
    random_sleep();
    print("crawl... ", list_page_url)
    global startup_count
    content = urllib2.urlopen(list_page_url).read()
    p_urls = re.compile('''<p class="title"><a target="_blank" href="([^>]*)"><span>([^<]*)''', re.IGNORECASE|re.DOTALL);

    urls = p_urls.finditer(content)
    for url in urls:
        startup_count += 1
        print("\n", startup_count, ": ", url.group(1), "\t", url.group(2))
        crawl_detail_page(url.group(1))


detail_rules = [\
["website", '''<a href="([^"]*)" target="_blank" class="weblink">'''], \
["name", '''<div class="line-title">\s*<span class="title">\s*<b>([^<]*)'''], \
["fund_status", '''获投状态</h2>\s*<p id="company-fund-status"><a class="btn btn-orange" href=".*?">(.*?)</a></p>'''], \
["tag", '''<a href="http://itjuzi.com/tag+.*?">(.*?)</a>'''], \
["setup_time", '''<li>时间:  <em>(.*?)</em></li>'''], \
["place", '''<li>地点:  <a href=".*?">(.*?)</a>,<em>(.*?)</em></li>'''], \
["motion", '''<li>状态:  <a href=".*?">(.*?)</a>
                        </li>'''], \
["founder", '''<tr>
             <td style="width:50px;"><a href=".*?"> <img src=".*?" width="50" height="50" alt=".*?" title=".*?" /> </a></td>
             <td style="width:70px;"><a href=".*?">(.*?)</a></td>
             <td style="width:70px;">(.*?)</td>
             <td style="width:140px;">
                         </td>
            <!-- <td>'''], \
["introduction", '''<li>简介:  <em>(.*?)</em></li>'''], \
["founder_intro", '''<tr>
             <td style="width:50px;"><a href=".*?"> <img src=".*?" width="50" height="50" alt=".*?" title=".*?" /> </a></td>
             <td style="width:70px;"><a href="(.*?)">.*?</a></td>
             <td style="width:70px;">.*?</td>
             <td style="width:140px;">
                         </td>
            <!-- <td>'''], \
["fund_needs", '''<h2>融资需求</h2>\s*<p id="company-fund-status"><a class="btn btn-orange" href=".*?">(.*?)</a></p>'''], \
 ]
 
detail_child_rules = [\
["fund_item", '''(<div class="company-fund-item">.*?</div>)'''], \
["fund_round", '''<div class="company-fund-item">\s*<h3><b class="pull-right">(.*?)</b>'''], \
["fund_date", '''<h3><b class="pull-right">.*?</b> (.*?)</h3>\s*<p class="company-fund-item-money text-center">'''], \
["fund_money", ''' <p class="company-fund-item-money text-center">\s*<a target="blank" href=".*?">(.*?)</a>'''], \
["fund_vc_company", '''<a href="http://itjuzi.com/investfirm/.*?">(.*?)</a>'''], \
 ]
def crawl_detail_page(detail_page_url):
    global body
    random_sleep();
    #content = urllib2.urlopen(detail_page_url).read()
    content = urllib.request.urlopen(detail_page_url).read()
    
    rowData = []
    for rule in detail_rules:
        value = extract_attibute(content, rule[1])
        print(rule[0], ": ", value)
        rowData.append(value)
    for rule in detail_child_rules[1:]:
        rowData.append("")
        
    body.append(rowData)

    #判断是否存在多笔投资？
    pattern = re.compile(detail_child_rules[0][1], re.IGNORECASE|re.DOTALL);
    matches = pattern.finditer(content)
    for match in matches:
        fund_item = match.group(1)
        row_fund_item_data = []
        for rule in detail_rules:
            row_fund_item_data.append("")
        for rule in detail_child_rules[1:]:
            value = extract_attibute(fund_item, rule[1])
            print(rule[0], ": ", value)
            row_fund_item_data.append(value)
        body.append(row_fund_item_data)

def get_founder_intro(content):
    return "TODO"
        
def extract_head():
    result = []
    for rule in detail_rules:
        result.append(rule[0])
    for rule in detail_child_rules[1:]:
        result.append(rule[0])
    return result


def extract_attibute(content, pattern_string):
    result = ""
    pattern = re.compile(pattern_string, re.IGNORECASE|re.DOTALL);
    matches = pattern.finditer(content)
    for match in matches:
        if len(result) > 0:
            result += "\n"
        for value in match.groups():
            if len(result) > 0:
                result = result + " "
            result += value.strip()

    return result

def random_sleep():
    random_sleep_ms = randint(1300,2000)
    time.sleep(random_sleep_ms/1000.0)


if __name__ == "__main__":
    main()

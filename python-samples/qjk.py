import urllib.request
import re
import http.cookiejar
import getopt
import xlrd
import xlwt3 as xlwt
import csv
import sys
import os
import datetime
from bs4 import BeautifulSoup

#import test_export


startup_count = 0
body = []

def main():
        login_itjuzi()
        target_url = 'http://www.itjuzi.com/company?tag=298&page='
        page_number_begin = 1
        page_number_end = 2
        excel_name = 'security_startup.xls'

        page_number = page_number_begin
        
        while page_number <= page_number_end:
            try:
                crawl_list_page(target_url + str(page_number))
                page_number +=1
                print('startup_count: ',startup_count)
            except Exception as e:
                print('craw failed--',e)
        #print(body)
        save_excel(excel_name, extract_head(), body)
    

def login_itjuzi():
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
    # 确认登录成功
    test_url = 'https://www.itjuzi.com/user/edit/basic'
    after_login_page = urllib.request.urlopen(test_url).read()
    p_username = re.compile('<input type="text" name="username" value="(.*?)" class="width-l"  />', re.IGNORECASE|re.DOTALL);
    username_from_page = p_username.search(str(after_login_page))
    if username_from_page is not None:
        print("################## login: ", username_from_page.group(1))

def crawl_list_page(list_page_url):
    print('crawl... ',list_page_url)
    global startup_count
    content = urllib.request.urlopen(list_page_url).read()
    p_urls = re.compile('<p class="title"><a target="_blank" href="([^>]*)"><span>([^<]*)',re.IGNORECASE|re.DOTALL)

    urls = p_urls.finditer(str(content))
    for url in urls:
        startup_count +=1
        print('\n', startup_count, ': ', url.group(1))
        res_data = {}     
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')       
        #<p class="title"><a target="_blank" href="http://www.itjuzi.com/company/31487"><span>易达大数据</span></a></p>
        name_node = soup.find('p', class_="title").find(target="_blank")
        print(name_node)
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        #summary_node = soup.find("div",class_="lemma-summary")
        #res_data['summary'] = summary_node.get_text()
        
        #return res_data

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
    content = urllib.request.urlopen(detail_page_url).read()

    rowData = []
    #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    name_node = soup.find(class_="line-title").find('b')
    #res_data['name'] = title_node.get_text()
    print('输出 node')
    print(name_node.get_text)
    #print(res_data['name'])

    for rule in detail_rules:
        value = extract_attibute(str(content), rule[1])
        print(rule[0],': ',value)
        rowData.append(value)
    for rule in detail_child_rules[1:]:
        rowData.append("")

    body.append(rowData)

    #判断是否存在多笔投资
    pattern = re.compile(detail_child_rules[0][1], re.IGNORECASE|re.DOTALL);
    matches = pattern.finditer(str(content))
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

        
def extract_head():
    result = []
    for rule in detail_rules:
        result.append(rule[0])
    for rule in detail_child_rules[1:]:
        result.append(rule[0])
    return result


def extract_attibute(content, pattern_string):
    result = ""
    #print(pattern_string)
    pattern = re.compile(pattern_string, re.IGNORECASE|re.DOTALL);
    matches = pattern.finditer(str(content))
    for match in matches:
        if len(result) > 0:
            result += "\n"
        for value in match.groups():
            if len(result) > 0:
                result = result + " "
            result += value.strip()

    return result

def save_excel(excel_name, head, body):
    wb = xlwt.Workbook(encoding='utf-8')

    ws = wb.add_sheet("itjuzi")

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
        num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    for headColumn, headValue in enumerate(head):
        ws.write(0, headColumn, headValue)

    for row, rowData in enumerate(body):
        for column, columnData in enumerate(rowData):
            ws.write(row+1, column, columnData)

    wb.save(excel_name)
    print("Output Excel File Saved!")


if __name__ == "__main__":
    main()


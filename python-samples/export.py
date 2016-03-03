#!/usr/bin/python
#coding=utf-8

#import xlrd, xlwt
import xlwt
import csv
import sys
import os
import datetime
import re

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
    if len(sys.argv) < 1:
        print('export.py output.xls')
        sys.exit(2)
    save_excel(sys.argv[1], ["website", "name"], [["a.com", "aaa"], ["b.com", "bbb"]])

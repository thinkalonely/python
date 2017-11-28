# /usr/bin/env python
# -*- utf-8 -*-

import os
from openpyxl import load_workbook
from datetime import date, timedelta

xls_path = 'E:\\test\\office'
all_day = []

# 获取日期
def get_day():
    today = date.today() 
    firstday = date(2017, 10, 20)
    delta = timedelta(1) # 间隔 1天
    day = firstday
    while day <= today:
        if day.weekday() < 5: # 工作日
            all_day.append(day)
        day = day + delta

def create_xls():
    for date in all_day:
        os.system('E: && cd %s && copy test.xlsx test%s.xlsx' % (xls_path, date))

def read_xls():
    for day in all_day:
        #print(day)
        file = '%s\\test%s.xlsx' % (xls_path, day)
        wb = load_workbook(filename=file)
        ws = wb.get_sheet_by_name('Sheet1')  # 获取特定的 worksheet
        # 通过坐标设置单元格值
        ws.cell(row=1, column=4).value = '%s' % day
        ws.cell(row=4, column=4).value = 'TEST-%s.sql' % day
        print(ws.cell(row=4, column=4).value)
        wb.save(file)
if name == "__main__"():
    get_day()
    create_xls()
    read_xls()

# -*- coding:utf-8 -*-
import datetime

def date_format():
    return "%Y%m%d"

def today_date():
    date=datetime.datetime(
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        0,0,0
    )
    return date.strftime(date_format())

# 控制台读入一个指定格式的日期
# 如果输入为空，自动设置日期为今天的凌晨0点
def input_date(info):
    print(info)
    while True:
        date_str=input(f"Please Input Date({date_format()}):")
        if date_str.strip()=="":
            date=today_date()
            print("Date Is ",date)
            return date
        else:
            try:
                date=datetime.datetime.strptime(date_str,date_format())
                print("Date Is",date)
                return date_str
            except ValueError:
                print("Input Date Error,Try Again!")
                continue
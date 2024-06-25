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

def current_week_first_day_date():
    today=datetime.datetime.today()
    week_start=today-datetime.timedelta(days=today.weekday())
    return week_start.strftime(date_format())

def current_week_last_day_date():
    today=datetime.datetime.today()
    week_end=today+datetime.timedelta(days=6-today.weekday())
    return week_end.strftime(date_format())

def current_month_first_day_date():
    today=datetime.datetime.today()
    month_start=today.replace(day=1)
    return month_start.strftime(date_format())

def current_month_last_day_date():
    today=datetime.datetime.today()
    month_end=(today.replace(day=1)+datetime.timedelta(days=32)).replace(day=1)-datetime.timedelta(days=1)
    return month_end.strftime(date_format())

def current_year_first_day_date():
    today=datetime.datetime.today()
    year_start=today.replace(month=1,day=1)
    return year_start.strftime(date_format())

def current_year_last_day_date():
    today=datetime.datetime.today()
    year_end=(today.replace(month=1,day=1)+datetime.timedelta(days=366)).replace(month=1,day=1)-datetime.timedelta(days=1)
    return year_end.strftime(date_format())

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
                print("Date Is",date_str)
                return date_str
            except ValueError:
                print("Input Date Error,Try Again!")
                continue

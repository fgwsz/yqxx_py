# -*- coding:utf-8 -*-
import os
import datetime
import re
import docx
import pyperclip
from yqxx import ext_date
from yqxx import config
from yqxx import common

# 得到当前文件夹下文件名在日期区间[start_date,end_date]之内的文件名列表
def data_file_list_in_date_range(start_date,end_date):
    start_date=datetime.datetime.strptime(start_date,ext_date.date_format())
    end_date=datetime.datetime.strptime(end_date,ext_date.date_format())
    file_list=[]
    for file in os.listdir(config.data_dir_path()):
        if file.endswith('.docx')and re.match(r'\d{8}',file):
            file_date=datetime.datetime.strptime(file[:8],ext_date.date_format())
            if start_date<=file_date<=end_date:
                file_list.append(file)
    return file_list

# 统计信息(业务逻辑)
# docx文件中存在的表格信息:
# 第1个(index=0)表格的第2列(index=1)表示市报送信息数量
# 第2个(index=0)表格的第2列(index=1)表示省报送信息数量
def count_docx_info(file_path):
    ret=[]
    if file_path.endswith('.docx'):
        docx_file=docx.Document(file_path)
        tables=docx_file.tables
        row=0
        count=0
        print('文件:',file_path)
        for table in tables:
            count=common.count_non_empty_cells_in_column(table,1)
            if row==0:
               print('市级报送信息数量:',count)
#            if row==1:
#               print('省级报送信息数量:',count)
            ret.append(count)
            row+=1
    return ret

def total_info_impl(begin_date,finish_date,paste_flag):
    files=data_file_list_in_date_range(begin_date,finish_date)
    count=[0,0]
    for file in files:
        file_count=count_docx_info(config.data_dir_path()+'/'+file)
        if len(file_count)==2:
            count[0]+=file_count[0]
            count[1]+=file_count[1]

    if begin_date==finish_date:
        text=f'{ext_date.today_date()}报送情况统计\n'
    else:
        text=f'区间日期[{begin_date},{finish_date}]报送情况统计\n'

    text=text+f'市级报送信息数量总计:{count[0]}\n'
#    text=text+f'省级报送信息数量总计:{count[1]}\n'
    print(text)
    if paste_flag:
        pyperclip.copy(text)

class TotalFlag:
    today_=0
    current_week_=1
    current_month_=2
    current_year_=3
    range_=4

def total_info(total_flag,paste_flag):
    if total_flag==TotalFlag.today_:
        begin_date=ext_date.today_date()
        finish_date=ext_date.today_date()
    elif total_flag==TotalFlag.current_week_:
        begin_date=ext_date.current_week_first_day_date()
        finish_date=ext_date.current_week_last_day_date()
    elif total_flag==TotalFlag.current_month_:
        begin_date=ext_date.current_month_first_day_date()
        finish_date=ext_date.current_month_last_day_date()
    elif total_flag==TotalFlag.current_year_:
        begin_date=ext_date.current_year_first_day_date()
        finish_date=ext_date.current_year_last_day_date()
    elif total_flag==TotalFlag.range_:
        begin_date=ext_date.input_date('请输入开始日期')
        finish_date=ext_date.input_date('请输入截止日期')

    total_info_impl(begin_date,finish_date,paste_flag)

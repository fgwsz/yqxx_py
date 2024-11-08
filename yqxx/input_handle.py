# -*- coding:utf-8 -*-
import re
import webbrowser
import subprocess
import pyperclip
from yqxx import config
from yqxx import ext_file
from yqxx import ext_string

g_url_pattern=0

def init():
    global g_url_pattern
    g_url_pattern=re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

def url_pattern():
    global g_url_pattern
    return g_url_pattern

#处理失败返回None
def input_handle(is_from_input_file=True):
    if is_from_input_file:
        #从输入文件读取输入
        input_content=ext_file.read_content(config.input_file_path())
    else:
        #从剪切板读取输入
        input_content=pyperclip.paste()

    if ext_string.is_blank(input_content):
        print('[FAIL][INPUT_HANDLE]: input file content is blank!')
        return False

    #提取链接
    url=ext_string.match_first(input_content,url_pattern())
    if ext_string.is_blank(url):
        print('[FAIL][INPUT_HANDLE]: url not found!')
        return False

    #把剩下的部分作为标题
    title=ext_string.remove_all(input_content,url_pattern())
    title=ext_string.remove_blank(title)

    #把单位信息去掉，防止造成属地干扰
    title=ext_string.remove_all(title,'单位：山东省德州市平原县委宣传部')
    title=ext_string.remove_all(title,'单位:山东省德州市平原县委宣传部')

    #获取属地信息
    location_list=[
        '德城','陵城','禹城','乐陵','临邑','平原','夏津',
        '武城','庆云','宁津','齐河','天衢'
    ]
    location_default='德州'
    location=location_default
    location_count=0
    for location_item in location_list:
        if location_item in title:
            if location_count==0:
                location=location_item
            else:
                location+="、"+location_item #多个属地一起拼接
            location_count+=1

    #删除多余信息
    title=ext_string.remove_all(title,'标题:')
    title=ext_string.remove_all(title,'标题：')
    title=ext_string.remove_all(title,'链接:')
    title=ext_string.remove_all(title,'链接：')
    title=ext_string.remove_all(title,r'摘要:\S*')
    title=ext_string.remove_all(title,r'摘要：\S*')

    #打开链接
    webbrowser.open(url)

    #拼接得到处理结果
    handle_result= \
        location+' : '+title+'\n'+ \
        url
    print(f'[PASS][INPUT_HANDLE][RESULT]\n{handle_result}')
    #复制结果到剪切板
    pyperclip.copy(handle_result)

    #清空输入文件
    if is_from_input_file:
        ext_file.write_content(config.input_file_path(),'')

    return True

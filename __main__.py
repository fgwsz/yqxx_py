# -*- coding:utf-8 -*-
import os
from . import input_handle
from . import push_info
from . import pop_info
from . import config
from . import total_info
from . import ext_string

def _open_data_file_of_today():
    os.startfile(config.data_file_path_of_today())

def _handle_text_of_info():
    input_handle.input_handle()

def _push_text_of_info():
    push_info.push_text_of_info()

def _push_image_of_info():
    push_info.push_image_of_info()

def _pop_info():
    pop_info.pop_info()

def _total_info_of_today():
    total_info.total_info(True,False)

def _total_info_of_today_and_copy():
    total_info.total_info(True,True)

def _total_info_of_date_range():
    total_info.total_info(False,False)

def _total_info_of_date_range_and_copy():
    total_info.total_info(False,True)

def _quit():
    exit()

def main():
    callback_dict={
        'o' :_open_data_file_of_today,
        'h' :_handle_text_of_info,
        't' :_push_text_of_info,
        'i' :_push_image_of_info,
        'd' :_pop_info,
        'tt':_total_info_of_today,
        'tc':_total_info_of_today_and_copy,
        'r' :_total_info_of_date_range,
        'rc':_total_info_of_date_range_and_copy,
        'q' :_quit
    }
    last_command=''
    while True:
        print("""
+command=callback=========================+
|o      |open data file of today          |
|h      |handle text of info              |
|t      |push text of info                |
|i      |push image of info               |
|d      |pop info                         |
|tt     |total info of today              |
|tc     |total info of today and copy     |
|r      |total info of date range         |
|rc     |total info of date range and copy|
|q      |quit                             |
+command=callback=========================+
        """)
        print(f"last command> {last_command}")
        command=input("input command> ")
        command=ext_string.remove_blank(command)
        last_command=command
        if command in callback_dict:
            callback_dict[command]()

if __name__=='__main__':
    main()

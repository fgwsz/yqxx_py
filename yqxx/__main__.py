# -*- coding:utf-8 -*-
from yqxx import ext_file
from yqxx import common
from yqxx import input_handle
from yqxx import push_info
from yqxx import pop_info
from yqxx import config
from yqxx import total_info
from yqxx import ext_string

def _open_data_file_of_today():
    common.data_file_of_today_create()
    ext_file.startfile(config.data_file_path_of_today())

def _handle_text_of_info():
    return input_handle.input_handle(False)

def _push_text_of_info():
    return push_info.push_text_of_info()

def _handle_and_push_text_of_info():
    if _handle_text_of_info():
        _push_text_of_info()

def _push_image_of_info():
    return push_info.push_image_of_info()

def _pop_info():
    return pop_info.pop_info()

def _total_info_of_today():
    return total_info.total_info(total_info.TotalFlag.today_,False)

def _total_info_of_today_and_copy():
    return total_info.total_info(total_info.TotalFlag.today_,True)

def _total_info_of_current_week():
    return total_info.total_info(total_info.TotalFlag.current_week_,False)

def _total_info_of_current_week_and_copy():
    return total_info.total_info(total_info.TotalFlag.current_week_,True)

def _total_info_of_current_month():
    return total_info.total_info(total_info.TotalFlag.current_month_,False)

def _total_info_of_current_month_and_copy():
    return total_info.total_info(total_info.TotalFlag.current_month_,True)

def _total_info_of_current_year():
    return total_info.total_info(total_info.TotalFlag.current_year_,False)

def _total_info_of_current_year_and_copy():
    return total_info.total_info(total_info.TotalFlag.current_year_,True)

def _total_info_of_date_range():
    return total_info.total_info(total_info.TotalFlag.range_,False)

def _total_info_of_date_range_and_copy():
    return total_info.total_info(total_info.TotalFlag.range_,True)

def _quit():
    exit()

def main():
    callback_dict={
        'o' :_open_data_file_of_today,
        'h' :_handle_text_of_info,
        't' :_push_text_of_info,
        'ht':_handle_and_push_text_of_info,
        'i' :_push_image_of_info,
        'd' :_pop_info,
        'tt':_total_info_of_today,
        'tc':_total_info_of_today_and_copy,
        'w' :_total_info_of_current_week,
        'wc':_total_info_of_current_week_and_copy,
        'm' :_total_info_of_current_month,
        'mc':_total_info_of_current_month_and_copy,
        'y' :_total_info_of_current_year,
        'yc':_total_info_of_current_year_and_copy,
        'r' :_total_info_of_date_range,
        'rc':_total_info_of_date_range_and_copy,
        'q' :_quit
    }
    last_command=''
    while True:
        print( \
"""+command=callback============================+
|o      |open data file of today             |
|h      |handle text of info                 |
|t      |push text of info                   |
|ht     |handle and push text of info        |
|i      |push image of info                  |
|d      |pop info                            |
|tt     |total info of today                 |
|tc     |total info of today and copy        |
|w      |total info of current week          |
|wc     |total info of current week and copy |
|m      |total info of current month         |
|mc     |total info of current month and copy|
|y      |total info of current year          |
|yc     |total info of current year and copy |
|r      |total info of date range            |
|rc     |total info of date range and copy   |
|q      |quit                                |
+command=callback============================+""")
        print(f"last command> {last_command}")
        command=input("input command> ")
        command=ext_string.remove_blank(command)
        last_command=command
        if command in callback_dict:
            callback_dict[command]()

if __name__=='__main__':
    main()

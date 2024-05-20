# -*- coding:utf-8 -*-
import os
from . import ext_date

def root_dir_path():
    return os.path.abspath(
        os.path.dirname(os.path.abspath(__file__))
    )

def input_file_path():
    return root_dir_path()+'/input.txt'

def data_dir_path():
    return root_dir_path()+'/data'

def data_file_path_of_today():
    return data_dir_path()+'/'+ext_date.today_date()+'.docx'

def data_file_path_of_template():
    return root_dir_path()+'/template.docx'

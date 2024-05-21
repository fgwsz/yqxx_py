# -*- coding:utf-8 -*-
import os
import sys
from yqxx import ext_date

def parent_path(path):
    return os.path.abspath(
        os.path.dirname(path)
    )

def root_dir_path():
    return parent_path(os.path.abspath(sys.argv[0]))

def input_file_path():
    return parent_path(root_dir_path())+'/input.txt'

def data_dir_path():
    return parent_path(root_dir_path())+'/data'

def data_file_path_of_today():
    return data_dir_path()+'/'+ext_date.today_date()+'.docx'

def data_file_path_of_template():
    return parent_path(root_dir_path())+'/template/template.docx'

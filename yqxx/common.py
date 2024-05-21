# -*- coding:utf-8 -*-
import os
import shutil
from yqxx import config

def count_non_empty_cells_in_column(table,column_index):
    count=0
    for row in table.rows:
        cell=row.cells[column_index]
        if cell.text.strip():
            count+=1
    return count

def data_file_of_today_create():
    if not os.path.exists(config.data_file_path_of_today()):
        shutil.copy(
            config.data_file_path_of_template(),
            config.data_file_path_of_today()
        )

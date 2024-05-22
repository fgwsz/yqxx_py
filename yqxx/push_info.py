# -*- coding:utf-8 -*-
import os
import docx
import pyperclip
import platform
import subprocess
from PIL import Image
from io import BytesIO
from yqxx import config
from yqxx import common

def image_grabclipboard_and_save(image_path):
    system_type=platform.system()
    ret=False
    if system_type=='Linux':
        import sys
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtGui import QClipboard, QImage
        app=QApplication(sys.argv)
        clipboard=app.clipboard()
        # 获取剪贴板中的图像类型
        mime_data=clipboard.mimeData()
        if mime_data.hasImage():
            image=clipboard.image()
            image.save(image_path)
            ret=True
        else:
            print('剪切板中没有图像数据')
        app.exit()
    else:
        from PIL import ImageGrab
        image=ImageGrab.grabclipboard()
        if image is None:
            print('剪切板中没有图像数据')
        else:
            image.save(image_path,'PNG')
            ret=True
    return ret

def image_save(image,image_path,ext):
    if system_type=='Linux':
        import pyscreenshot
        image.save(image_path,ext)
    else:
        from PIL import ImageGrab
        image.save(image_path,ext)

def push_text_of_info(index_of_table=0):
    common.data_file_of_today_create()
    document=docx.Document(config.data_file_path_of_today())
    table=document.tables[index_of_table]
    cell_col=1
    cell_row=common.count_non_empty_cells_in_column(table,cell_col)
    cell=table.cell(cell_row,cell_col)
    clipboard_text=pyperclip.paste()
    cell.text=clipboard_text
    document.save(config.data_file_path_of_today())
    print(f'{config.data_file_path_of_today()} table[{index_of_table}] index[{cell_row}] 添加文本成功!')

def push_image_of_info(index_of_table=0):
    common.data_file_of_today_create()
    image_path=config.root_dir_path()+'/__clipboard_image__.png'
    if not image_grabclipboard_and_save(image_path):
        return False

    document=docx.Document(config.data_file_path_of_today())
    table=document.tables[index_of_table]
    cell_col=1
    cell_row=common.count_non_empty_cells_in_column(table,cell_col)
    if(cell_row==0):
        return False
    cell=table.cell(cell_row-1,cell_col)
    paragraph=cell.add_paragraph()
    paragraph.add_run().add_picture(image_path,width=cell.width)
    document.save(config.data_file_path_of_today())
    if os.path.exists(image_path):
        os.remove(image_path)
    print(f'{config.data_file_path_of_today()} table[{index_of_table}] index[{cell_row-1}] 添加图片成功!')

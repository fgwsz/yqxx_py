# -*- coding:utf-8 -*-
import os
import platform
import subprocess

def read_content(file_path):
    file=open(file_path,'r')
    file_content=file.read()
    file.close()
    return file_content

def write_content(file_path,content):
    file=open(file_path,'w')
    file.write(content)
    file.close()

def startfile(file_path):
    system=platform.system()
    if system=='Windows':
        os.startfile(file_path)
    elif system=='Linux':
        subprocess.Popen(['xdg-open',file_path])
    else:
        raise NotImplementedError(f'Unsupported platform: {system}')

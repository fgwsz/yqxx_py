# -*- coding:utf-8 -*-
def read_content(file_path):
    file=open(file_path,'r')
    file_content=file.read()
    file.close()
    return file_content

def write_content(file_path,content):
    file=open(file_path,'w')
    file.write(content)
    file.close()

# -*- coding:utf-8 -*-
import re

def remove_blank(string):
    return ''.join(string.split())

def is_blank(string):
    return remove_blank(string)==''

def match_first(string,regex_pattern):
    result=re.search(regex_pattern,string)
    if result is None:
        return ''
    else:
        return result.group()

def replace_all(string,regex_pattern,sub_string):
    return re.sub(regex_pattern,sub_string,string)

def remove_all(string,regex_pattern):
    return replace_all(string,regex_pattern,'')
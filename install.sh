#!/bin/bash
if ! pip show pyperclip &> /dev/null; then
    pip install pyperclip
fi
if ! dpkg -l xclip &> /dev/null; then
    sudo apt-get install xclip #for linux pyperclip
fi

if ! pip show python-docx &> /dev/null; then
    pip install python-docx
fi

if ! pip show Pillow &> /dev/null; then
    pip install Pillow
fi

if ! pip show pyqt5 &> /dev/null; then
    pip install pyqt5 # -i https://pypi.tuna.tsinghua.edu.cn/simple/
    # download fast url
fi

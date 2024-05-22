#!/bin/bash
if ! pip show pyperclip &> /dev/null; then
    pip install pyperclip
fi
sudo apt-get install xclip #for linux pyperclip

if ! pip show python-docx &> /dev/null; then
    pip install python-docx
fi

if ! pip show Pillow &> /dev/null; then
    pip install Pillow
fi
pip install pyqt5

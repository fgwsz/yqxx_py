#!/bin/bash
if ! pip show pyperclip &> /dev/null; then
    pip install pyperclip
fi
if ! pip show python-docx &> /dev/null; then
    pip install python-docx
fi
if ! pip show Pillow &> /dev/null; then
    pip install Pillow
fi

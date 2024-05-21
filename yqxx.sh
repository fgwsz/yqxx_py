#!/bin/bash
YQXX_MODULE_DIR=$(dirname "$(readlink -f "$0")")
cd $YQXX_MODULE_DIR
if ! pip show pyperclip &> /dev/null; then
    pip install pyperclip
fi
if ! pip show python-docx &> /dev/null; then
    pip install python-docx
fi
if ! pip show Pillow &> /dev/null; then
    pip install Pillow
fi
if ! type python &> /dev/null; then
    python3 -m yqxx
else
    python -m yqxx
fi

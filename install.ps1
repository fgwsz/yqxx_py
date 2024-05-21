if(-not(pip show pyperclip 2>&1)){
    pip install pyperclip
}
if(-not(pip show python-docx 2>&1)){
    pip install python-docx
}
if(-not(pip show Pillow 2>&1)){
    pip install Pillow
}

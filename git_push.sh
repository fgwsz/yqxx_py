#!/bin/bash
git add ./data/.gitkeeper
git add ./template/template.docx
git add ./yqxx/*.py
git add ./input.txt
git add ./*.sh
git add ./*.ps1
read -p "Input Git Commit Info: " commit_info
git commit -m "$commit_info"
git push

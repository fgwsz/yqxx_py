git add ./data/.gitkeeper
git add ./template/template.docx
git add ./yqxx/*.py
git add ./input.txt
git add ./*.sh
git add ./*.ps1
$commit_info=Read-Host -Prompt "Input Git Commit Info"
git commit -m $commit_info
git push

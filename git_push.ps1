git add ./data/.gitkeeper
git add ./*.py
git add ./*.ps1
git add ./input.txt
git add ./template.docx
$commit_info=Read-Host -Prompt "Input Git Commit Info"
git commit -m $commit_info
git push

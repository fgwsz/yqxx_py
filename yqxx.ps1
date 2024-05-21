$MODULE_DIR=Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
Set-Location $MODULE_DIR
python -m yqxx

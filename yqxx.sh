#!/bin/bash
YQXX_MODULE_DIR=$(dirname "$(readlink -f "$0")")
cd $YQXX_MODULE_DIR
if ! type python &> /dev/null; then
    python3 -m yqxx
else
    python -m yqxx
fi

#!/bin/bash

python3 /usr/local/var/pyenv/shims/virtualenv env
. env/bin/activate
pip install -r requirements.txt

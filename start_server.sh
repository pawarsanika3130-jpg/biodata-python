#!/bin/bash

cd /home/ec2-user/biodata

pkill -f app.py || true

pip3 install -r requirements.txt

nohup python3 app.py > output.log 2>&1 &
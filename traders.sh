#! /bin/bash
set -e

echo $(date)

echo "running script..." >> ~/Desktop/traders/cron.log

cd ~/Desktop/traders

~/Desktop/traders/env/bin/python cli.py >> ~/Desktop/traders/cron.log

echo "script completed successfully" >> ~/Desktop/traders/cron.log
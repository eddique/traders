# Traders
A twitter bot for tracking congressional stock transactions.

# Secrets
Export the following values in your terminal session or add to a .env in the repo before running
```sh
export CONSUMER_KEY=<Your Twitter consumer key>
export CONSUMER_SECRET=<Your Twitter consumer secret>
export ACCESS_TOKEN=<Your Twitter access token>
export ACCESS_TOKEN_SECRET=<Your Twitter access token secret>
```

# Quick Start
```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

# Usage

The default command will check for the last fetched date, and query the period for public financial disclosures from the last fetched date (or 24 hours prior if not exists) until execution time.
```sh
python cli.py
```
Fetches transactions since last fetched date and prints to stdout, but will not post to Twitter
```sh
python cli.py -c
```

# Configuration

Clone the repo and copy the run script to the root directory
```sh
mkdir ~/Desktop/traders && cd ~/Desktop/traders
git clone https://github.com/eddique/traders .
cp traders.sh ~/
```

Open crontab and set cronjobs for periodic runs
```sh
VISUAL=nvim crontab -e
```
```sh
0 9 * * * ~/traders.sh > ~/Desktop/traders/cron.log 2>&1
0 12 * * * ~/traders.sh > ~/Desktop/traders/cron.log 2>&1
0 17 * * * ~/traders.sh > ~/Desktop/traders/cron.log 2>&1
```
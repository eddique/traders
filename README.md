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
Running locally
```sh
mkdir ~/Desktop/traders && cd ~/Desktop/traders
```
```sh
git clone https://github.com/eddique/traders .
```
```sh
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
```sh
VISUAL=nvim crontab -e
```
```sh
0 9 * * * ~/Desktop/traders/run.sh
0 12 * * * ~/Desktop/traders/run.sh
0 17 * * * ~/Desktop/traders/run.sh
```
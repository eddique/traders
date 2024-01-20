# Traders
A twitter bot for tracking congressional stock transactions.

# Usage

The default command will check for the last fetched date, and query the period for public financial disclosures from the last fetched date (or 24 hours prior if not exists) until execution time.
```sh
python cli.py
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
VISUAL=nvim crontab -e
```
```sh
0 9 * * * ~/Desktop/traders/env/bin/python ~/Desktop/traders/cli.py
0 12 * * * ~/Desktop/traders/env/bin/python ~/Desktop/traders/cli.py
0 17 * * * ~/Desktop/traders/env/bin/python ~/Desktop/traders/cli.py
```

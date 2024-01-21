from lib import app
import argparse
def run():
    parser = argparse.ArgumentParser(description="A CLI for managing financial twitter posts")
    parser.add_argument("--check", "-c", action="store_true", help="A CLI for managing financial twitter posts")
    args = parser.parse_args()
    if args.check:
        app.check()
    else:
        app.report_txs()
import os
import csv
from datetime import datetime, timedelta

PATH="metadata.csv"

def generate_range() -> tuple[str]:
    return (start(), now())


def now() -> str:
    now = datetime.now()
    formatted_date = now.strftime("%m/%d/%Y %H:%M:%S")
    return formatted_date
def start() -> str:
    if os.path.exists(PATH):
        with open(PATH, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    return row['last_checked']
    else:
        delta = datetime.now() - timedelta(days=1)
        formatted_date = delta.strftime("%m/%d/%Y %H:%M:%S")
        return formatted_date

def set_metadata(start: str):
    with open(PATH, mode="w", newline="") as file:
        columns = ["last_checked"]
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerow([start])

def format_txs(txs: list[dict[str]]) -> list[str]:
    messages = []
    for tx in txs:
        message = f"""New Trade Alert
name: {tx["first_name"]} {tx["last_name"]}
ticker: ${tx["ticker"]}
order: {tx["order_type"]}
amount: {tx["tx_amount"]}
transaction date: {tx["tx_date"]}
reported on: {tx["received"]}
"""
        messages.append(message)
    return messages
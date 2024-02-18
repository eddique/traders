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
        message = f"""New Trade Alert {order_emoji(tx["order_type"])} {amount_emoji(tx["tx_amount"])}
{tx["first_name"]} {tx["last_name"]}
${tx["ticker"]}
{tx["order_type"]}
{tx["tx_amount"]}
transaction date: {tx["tx_date"]}
reported on: {tx["received"]}
#traders #{tx["first_name"].split(" ")[0]}{tx["last_name"]} #{tx["ticker"]}
"""
        messages.append(message)
    return messages

def order_emoji(order_type: str) -> str:
    return "📉" if "Sale" in order_type else "📈"

def amount_emoji(tx_amount: str) -> str:
    if "$15,000" in tx_amount:
        emoji = "🧐"
    elif "$50,000" in tx_amount:
        emoji = "🧐🧐"
    elif "$250,000" in tx_amount:
        emoji = "🧐🧐🧐"
    elif "$500,000" in tx_amount:
        emoji = "🧐🧐🧐🧐"
    elif "$1,000,000" in tx_amount:
        emoji = "🧐🧐🧐🧐🧐"
    else:
        emoji = "🧐"
    return emoji
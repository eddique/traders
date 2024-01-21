from lib import trades, twitter, utils

def report_txs():
    try:
        txs = trades.fetch_transactions()
        msgs = utils.format_txs(txs)
        for msg in msgs:
            twitter.create_tweet(msg)
        utils.set_metadata(utils.now())
    except Exception as e:
        print(e)
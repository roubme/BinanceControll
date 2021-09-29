import ccxt
import pandas as pd
import pprint
import time
import datetime

print('CCXT Version:', ccxt.__version__)

# binance = ccxt.binance()
# btc_ohlcv = binance.fetch_ohlcv("BTC/USDT")
#type(btc_ohlcv)
#print(btc_ohlcv)
#markets = binance.load_markets()
#btc = binance.fetch_ticker("BTC/USDT")
#for market in markets.keys():
#    if market.endswith("/USDT"):
#        print(market)
#pprint.pprint(btc)

#print("현재가", btc['last'])

# df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index(df['datetime'], inplace=True)

# symbol = "BTC/USDT"

# while True:
#    btc = binance.fetch_ticker(symbol)
#    now = datetime.datetime.now()
#    print(now, btc['last'])
#    time.sleep(1)





with open("api.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret  = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

order = binance.create_market_buy_order(
    symbol="DOT/USDT",
    amount=0.4
)

pprint.pprint(order)


# params = {
#    'test': True,  # test if it's valid, but don't actually place it
#}

# markets = binance.load_markets()
# markets = binance.load_markets()
# symbol = "DOT/USDT"
# market = binance.market(symbol)
# leverage = 2

# resp = binance.fapiPrivate_post_leverage({
#    'symbol': market['id'],
#    'leverage': leverage
#})

# symbol = symbol,
# type = 'limit',
# side = 'sell',
# amount = 0.1,
# price = 29.338

# exchange.options = {'defaultType': 'future', 'adjustForTimeDifference': True,'defaultTimeInForce':False}
# binance.options['defaultType'] = 'future'
# binance.options['adjustForTimeDifference'] = False
# binance.options['defaultTimeInForce'] = 'GTC'
# binance.set_sandbox_mode(enabled=True)
# binance.set_sandbox_mode(enabled=True)
# order = binance.create_order(symbol, type, side, amount, price, params)
#pprint.pprint(order)
# balance = binance.fetch_balance(params={"type": "future"})
# btc = binance.fetch_ticker("BTC/USDT")
# btc_ohlcv = binance.fetch_ohlcv(symbol='BTC/USDT', timeframe='1d', since=None, limit=10)
# print(balance['USDT'])
# print(api_key)
# print(secret)
# pprint.pprint(balance['total'])
# pprint.pprint(btc['last'])
# df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index('datetime', inplace=True)

# pprint.pprint(df)

# order_book = binance.fetch_order_book("BTC/USDT")
# asks = order_book['asks']
# bids = order_book['bids']

# pprint.pprint(asks[0])
# pprint.pprint(bids[0])
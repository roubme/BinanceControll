import ccxt
import pandas as pd
import pprint
import time
import datetime

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


# 파일로부터 apiKey, Secret 읽기
with open("api.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()

# binance 객체 생성
binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})
# markets = binance.load_markets()
markets = binance.load_markets()
symbol = "DOT/USDT"
market = binance.market(symbol)
leverage = 2

resp = binance.fapiPrivate_post_leverage({
    'symbol': market['id'],
    'leverage': leverage
})

order = binance.create_market_buy_order(
    symbol=symbol,
    amount=0.1,
)
pprint.pprint(order)
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
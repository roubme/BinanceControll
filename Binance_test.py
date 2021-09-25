import ccxt
import pandas as pd
import pprint

binance = ccxt.binance()
btc_ohlcv = binance.fetch_ohlcv("BTC/USDT")
#type(btc_ohlcv)
#print(btc_ohlcv)
#markets = binance.load_markets()
#btc = binance.fetch_ticker("BTC/USDT")
#for market in markets.keys():
#    if market.endswith("/USDT"):
#        print(market)
#pprint.pprint(btc)

#print("현재가", btc['last'])

df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df.set_index(df['datetime'], inplace=True)
print(df)
import ccxt
import pprint
import time
import pandas as pd

api_key = "0CtoAOdfUKM6UMpe4HbNJq5MQwNDzsdKMV9jbImdmFjZBmCO9RwCskT3dXgrYTNA"
secret = "VcdyMBBtjrCxdhkU1xR4INLaYFMJbm1zm9zWW5mTVgeDmFDQ8T3m4LAUD7dD0NXu"

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

order = binance.create_market_buy_order("DOT/USDT", 0.5)
print(order)
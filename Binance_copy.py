import ccxt
import pprint
with open("api.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()


exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': secret,
        'enableRateLimit': True,
    })
    # exchange.set_sandbox_mode(True)
params = {
    'test': True,  # test if it's valid, but don't actually place it
    }

symbol: str = "DOT/USDT"
type = 'limit'  # or 'market'
side = 'sell'  # or 'buy'
amount = 0.01
price: float = 29.581  # or None

    #exchange.options = {'defaultType': 'future', 'adjustForTimeDifference': True,'defaultTimeInForce':False}
exchange.options['defaultType'] = 'future'
exchange.options['adjustForTimeDifference'] = False
    #exchange.options['defaultTimeInForce'] = 'GTC'
exchange.set_sandbox_mode(enabled=True)

order = exchange.create_order(symbol, type, side, amount, price, params)
#print(order)
btc = exchange.fetch_ticker(symbol)
pprint.pprint(btc)
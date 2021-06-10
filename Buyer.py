from datetime import datetime
from binance.client import Client
from binance.exceptions import BinanceAPIException
'''
# This is the test account api
api_key = "Sjk3JBCXOLdxLJ6CndOW10jO8EUZVuoUrJr70kz557Szj8ae8OxABq5gd6Y59MCp"
api_secret = "99wmjDVkWuHrI5fsab7NNeKACR4wAGzYbA7PnXefGKxEY01bnF7LLxnTt4TgUuTl"
'''


# Original Echange Api
api_key = "ZV4QxddoSR6HkzQYrLIWOlp0BeJIapHrIuYnCt5Z2rsD98YLp8dhuO8Icb05pvew"
api_secret = "hWFfWYzB1FzSPzjvUSNN0g1Mw3vsK66Lq6tQlePy7fad7w7OozWLkPQYLPxwTmUP"


client = Client(api_key, api_secret)


Symbol = "GTCUSDT"
BuyAmount = 14 # in USDT
Type = "market"
Side = "buy"
Param = {"test": True} # Only while testing.
price = None # beacuse market order.

SecondDisplacemnet = 0
LaunchTimeStamp = {"Hour": 12, "Minute": 47}
              
Now = datetime.now()
LaunchTime = Now.replace(hour = LaunchTimeStamp["Hour"], 
                         minute = (LaunchTimeStamp["Minute"]-1), 
                         second = 58,
                         microsecond = 0) 
while True:
    Now = datetime.now()
    try:
        order = client.create_order(symbol = Symbol, side = Side, type = Type, quoteOrderQty=BuyAmount)
    except BinanceAPIException as e:
        print("Pair not listed yet", datetime.now())
    else:
        print(order["fills"])
        print("Now: ", Now, "Pre: ", LaunchTime)
        print("Time:", datetime.fromtimestamp(int(order["transactTime"])/1000))
        print("Timestamp: ", order["transactTime"])
        break
    
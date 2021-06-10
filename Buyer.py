from datetime import datetime
from binance.client import Client
from binance.exceptions import BinanceAPIException
'''
# This is the test account api
api_key = ""
api_secret = ""
'''

# Original Echange Api
api_key = ""
api_secret = ""

client = Client(api_key, api_secret)

Symbol = "ETHUSDT"
BuyAmount = 12 # in USDT
Type = "market"
Side = "buy"

FinishTask = False        
Now = datetime.now()
LaunchTime = Now.replace(hour = 19, 
                         minute = 8, 
                         second = 58,
                         microsecond = 0)
while True:
    Now = datetime.now()
    if Now > LaunchTime:
        while True:
            try:
                order = client.create_order(symbol = Symbol, side = Side, type = Type, quoteOrderQty=BuyAmount)
            except BinanceAPIException as e:
                print("Error: ", e.message, datetime.now())
            else:
                print(order["fills"])
                print("Now: ", Now, "Pre: ", LaunchTime)
                OrderTime = datetime.fromtimestamp(int(order["transactTime"])/1000)
                print("Time:", OrderTime)
                print("Time Difference: ", OrderTime - Now)
                FinishTask = True
                break
    if FinishTask:
        break

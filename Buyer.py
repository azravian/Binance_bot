from datetime import datetime
from binance.client import Client
from binance.exceptions import BinanceAPIException
'''
# This is the test account api
api_key = ""
api_secret = ""
'''

# Original Exchange Api

api_key = ""
api_secret = ""

client = Client(api_key, api_secret)

Symbol = "ETHUSDT" # Coin name with USDT 
BuyAmount = 36 # in USDT
Type = "market" # The order will be in market price
Side = "buy" # Buy Order

FinishTask = False # Flag variable for loop continuation  
Now = datetime.now() # Current date and time 
LaunchTime = Now.replace(hour = 19, # Launch date and time, suggested to keep 2 second less the actual launch time. 
                         minute = 8, # if launching at 16:00:00, set the time as 15:59:58
                         second = 58,
                         microsecond = 0)
while True: # Main loop, basically for time checking.
    Now = datetime.now() #Fetch the time continuously.
    if Now > LaunchTime: # when time is greater the set time.
        while True: # Second loop to send the order command concurrently
            print("Sending order at:", date.now())
            try:
                order = client.create_order(symbol = Symbol, side = Side, type = Type, quoteOrderQty=BuyAmount) # Order command
            except BinanceAPIException as e: # To handle exception and keeping code from crashing
                print("Error: ", e.message, datetime.now()) # prints the error message 
            else:
                print(order["fills"]) # The dteails of successful order
                print("Now: ", Now, "Pre: ", LaunchTime)
                OrderTime = datetime.fromtimestamp(int(order["transactTime"])/1000) # Time of Order execution
                print("Time:", OrderTime)
                print("Time Difference: ", OrderTime - Now) # The difference of sending order and execution of order.
                FinishTask = True # to break out of the main loop.
                break
    if FinishTask:
        break

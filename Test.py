from binance.client import Client
import datetime



api_key = "ZV4QxddoSR6HkzQYrLIWOlp0BeJIapHrIuYnCt5Z2rsD98YLp8dhuO8Icb05pvew"
api_secret = "hWFfWYzB1FzSPzjvUSNN0g1Mw3vsK66Lq6tQlePy7fad7w7OozWLkPQYLPxwTmUP"

client = Client(api_key, api_secret)
sum_all = 0
i = 0
for i in range(0, 20):
    print("iteration: ", i)
    Now = datetime.datetime.now()
    time_res = client.get_server_time()
    serverTime = datetime.datetime.fromtimestamp(int(time_res["serverTime"])/1000)
    print(Now, "Before Call")
    print(serverTime, "Server Time")
    latency = serverTime - Now
    print(latency, "Latency")
    print("======================================")
    sum_all += int(latency.microseconds) 


print("Avergae Latency is: ", sum_all/20, "microseconds")
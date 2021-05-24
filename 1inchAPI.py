import requests
import json
import os
import time
from datetime import datetime

scary_price = 4.5
good_price = 5.3
bound_range = 0.6

fromTokenAddress = "" #add token address
toTokenAddress = "" #add token address
scale_factor = 1000
req = "https://api.1inch.exchange/v3.0/56/quote?fromTokenAddress=" + fromTokenAddress + "&toTokenAddress=" + toTokenAddress + "&amount=" + str(scale_factor)


while True:
    try:
        response = requests.request("GET", req)
        data = response.json()
        current_price = float(data["toTokenAmount"]) / scale_factor
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        print(str(current_price) + " at " + date_time)
        if current_price <= scary_price or current_price > good_price:
            os.system("python3 alert.py")
            print("dang")
            scary_price = current_price - (bound_range/2)
            good_price = current_price + (bound_range/2)
            os.system("python3 textAlert.py " + str(current_price) + " " + str(scary_price) + " " + str(good_price))
            print("Lower: " + str(scary_price) + " | Upper: " + str(good_price))
    except:
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        print("something went wrong at " + date_time)
    time.sleep(60)

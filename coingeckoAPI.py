import requests
import json
import os
import time
from datetime import datetime

scary_price = 3.20
#good_price = 3.75
coin_name = ""

while True:
    response = requests.request("GET", "https://api.coingecko.com/api/v3/simple/price?ids=nerve-finance&vs_currencies=USD")
    data = response.json()
    current_price = float(data[coin_name]['usd'])
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(str(current_price) + " at " + date_time)
#if current_price <= scary_price or current_price >= good_price:
    if current_price <= scary_price:
        os.system("python3 send_email.py")
        print("dang")
        break
    time.sleep(60)
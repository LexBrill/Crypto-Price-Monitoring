import os
import sys
from twilio.rest import Client

current_price = float(sys.argv[1])
scary_price = float(sys.argv[2])
good_price = float(sys.argv[3])

client = Client("", "") #add your own API keys
numbers = ["", ""] #add numbers to call

for n in numbers:
    message = client.messages \
        .create(
            body="N: " + str(current_price) + " | L: " + str(scary_price) + " | U: " + str(good_price),
            from_="", #sending number
            to=n
        )
    print(message.sid)
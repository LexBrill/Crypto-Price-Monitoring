import os
from twilio.rest import Client

client = Client("", "") #add your own keys
twilio_number = '' #add your own number
numbers = ["", ""] #add list of numbers you want called

for n in numbers:
    call = client.calls.create(
        twiml = '<Response><Say>Check price</Say></Response>',
        to = n,
        from_= twilio_number
        )
    print(call.sid)
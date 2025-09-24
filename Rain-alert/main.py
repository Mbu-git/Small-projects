import os

import requests
from twilio.rest import Client

account_sid = "Your account sid from Twilio goes here"
auth_token = "authentication token from Twilio goes here"
ow_url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "Insert-API-key"

weather_params ={
    "appid" : api_key,
    "lat" : 45.828529,
    "lon" : 1.261750,
    "units": "metric",
    "cnt" : 4
}

response = requests.get(ow_url, params=weather_params)
response.raise_for_status()
w_data = response.json()

weather_ids = [entry["weather"][0]["id"] for entry in w_data["list"]]
print(weather_ids)
will_rain = False
for w_id in weather_ids:
    if w_id < 700:
        will_rain = True
    if will_rain:
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            body="It's going to rain, you may need an umbrella.",
            from_="Example: +1234556789 A number meant to send the sms from",
            to="The number to receive the sms",
        )
        print(message.status)

# These are the requests
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

######proxy client because it uses a trial version of pythonanywhere. it wont be needed if we use paid version#####
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

#Account sid and token given by to twilio
account_sid = "AC121cc84bac166b7b54c52d8b16379f62"
auth_token = 'bc60bf33a84f482a89611de7e7b11668'

#open weather API
urls = "https://api.openweathermap.org/data/2.5/onecall"

#parameters passed while calling tha API
parameters = {
    'lat': 28.4089,
    'lon': 77.3178,
    'appid': '7eead96bbe2bd091e641c9a0b90d5800',
    'exclude': "current,minutely,daily",  #forecasting based on hourly so exlude other
}
req = requests.get(urls, params=parameters)
response = req.json()
hourly = response['hourly'] # parse ohourly data

#it gives forecast for next 48 hour but we need only next 12 hour so.
for i in range(1, 13):
    weather = hourly[i]['weather'][0]['id']
    if weather < 700:
        print("bring an umbrella")
        #client of twilio to send message
        client = Client(account_sid, auth_token,http_client=proxy_client)

        message = client.messages \
                        .create(
        body="it will rain today",
        from_='+18454022616',
        to='+918882474233'
                 )
        print(message.status)
    # umbrella(weather)
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

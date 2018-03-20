from twilio.rest import Client
from m2x.client import M2XClient
from time import sleep

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token = ""
client = Client(account_sid, auth_token)
while True:
{% CODE %}
    sleep(10)

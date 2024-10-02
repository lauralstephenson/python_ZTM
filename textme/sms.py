#This is a program to send yourself a text message using Twilio API.
#I am using pseudocode so as not to give out private information.

#first import Twilio API credentials
from twilio.rest import Client

#this is Twilio's generated account sid and auth token
#either keep these in a private file or hash them
account_sid = "youraccountsid"
auth_token = "yourauthtoken"
client = client(account_sid, auth_token)

message = client.messages.create(
  from_="yourTwilionumber",
  body = "I can't belive this works!"
  to="yourPhoneNumber"
  )

print(message.sid)
#NTFY, pronounced Notify, no signups
#just use the requests import

import requests

#First pick a topic
#Then get notifications on your cell or computer as a desktop notification
#Can do PUT or POST
#it's also got a free app
#The topic IS a password, so pick something not easily guessable
requests.post("https://ntfy.sh/mytopic",
              data="Backup successful 😀".encode(encoding='utf-8'))
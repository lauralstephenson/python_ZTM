#A practice email program sender side
#use SMTP email sending protocol
import smtplib
#email message built into Python
from email.messages import EmailMessage
#this is a template for email message using $ for names
from string import Template
#library to read HTML files
from pathlib import Path

#lots of configuration
#this is our email project
#this is a template
html = Template(Path("index.html").read.text())
email = EmailMessage()
email["from"] = "Laura Stephenson"
email["to"] = "lstephenson556@gmail.com" #this will be the dummy account
email["subject"] = "You won a million dollars!"

email.set_content(html.substitute({name = "TinTin"}), "html")

#need to send it by logging in to our dummy gmail account
#and sending it

with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
  smtp.ehlo() #say hello to the server
  smtp.starttls() #encryption mechanism
  smtp.login("lstephenson556", "password") #change to the dummy account
  smtp.send_message(email)
  print("All good, Boss!")
  #check your spam folder when you send this
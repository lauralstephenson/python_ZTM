#Password Length Detector

#get username and password
username = input("What is your username? ")
userpassword = input("What is your password?")
length = len(userpassword)
hidden_password = "*" * length
#Give length of password
#Block username and print * instead
print(f"{username}, your password,  {hidden_password}, is {length} letters long.")
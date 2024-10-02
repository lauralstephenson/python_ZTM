# Error Handling
# This forces the user to enter an int
# This is a try block with except, else, and break
while True:
    try:
        age = int(input("What is your age? "))
        print(age)
    except ValueError:
        print("Please enter a number!")
         #creating your own error
    #raise ValueError("Hey, cut it out!")
    except ZeroDivisionError:
        print("Please enter a number higher than zero!")
    else:
        print("Thanks!")
        break

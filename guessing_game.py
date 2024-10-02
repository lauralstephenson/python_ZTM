from random import randint

# generate a # 1 to 10
answer = randint(1, 10)

while True:
    try:
        # input from user
        guess = int(input(f"Guess a number 1-10: "))
        # check that input is a # 1-10
        if 0 < guess < 11:
            if guess == answer:
                print("You are a genius!")
                break
        else:
            print("Hey, I said 1~10!")
            break
    except ValueError:
        print("Please enter a number!")
        continue
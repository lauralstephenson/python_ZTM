import random

# check that input is a # 1-10
def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("You are a genius!")
            return True
    else:
        print("Hey, I said 1~10!")

if __name__ == "__main__":
# generate a # 1 to 10
    answer = random.randint(1, 10)           
    while True:
        try:
        # input from user
            guess = int(input(f"Guess a number 1-10: "))
            if(run_guess(guess, answer)):
                break
        except ValueError:
            print("Please enter a number!")
            continue
from random import randint
import sys
# generate a number from 1~10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# take input from user

# check if the input is a number from the range
while True:
    try:
        guess = int(input("Guess a number in the range: "))
        if sys.argv[1] <= guess <= sys.argv[2]:
            # check if the number is a correct guess otherwise retry
            if guess == answer:
                print('You are a genius!')
                break
        else:
            print('Hey hey, I said from the range')
    except ValueError:
        print("Enter a valid number from the range :(")
        continue

    

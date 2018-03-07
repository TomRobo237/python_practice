import random, sys

def number_check(value):
    try:
        int(value)
        return 0
    except ValueError:
        print("Please enter your guess as a whole number.")
        return 1

def guess_try(number):
     if number < secret_num:
        print("No, that's too low.")
        return 1
     elif number > secret_num:
        print("Too High!")
        return 1
     else:
        return 0
    
secret_num = random.randint(1,20)
print("I'm thinking of a number between 1 and 20..")
guess=''
tried=0
while not guess:
    print("Guess?")
    guess= input()
    if guess == 'exit':
        print("Exiting...")
        sys.exit()
    if guess == '':
        print("No number entered!")
    if number_check(guess) == 0:
        tried += 1
        guess=int(guess)
        success=guess_try(guess)
        if success == 0:
            print("You got it!")
            print("It took you " + str(tried) + " times")
            sys.exit()
        else:
            guess=''        
    else:
        guess=''

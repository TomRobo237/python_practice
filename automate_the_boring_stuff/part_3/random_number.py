import random, sys, os, math

amount = ''
rand_top = ''
while not amount:
    print('How many random values would you like?')
    amount = input()
    if amount == 'exit':
        sys.exit()
    try:
        amount = int(amount)
        continue
    except ValueError:
        print('Please enter a whole number!\nIf you would like to quit, type exit.')
        amount = ''

while not rand_top:
    print('Maximum number?')
    rand_top = input()
    if rand_top == 'exit':
        sys.exit()
    try:
        rand_top = int(rand_top)
        continue
    except ValueError:
        print('Please enter a whole number!\nIf you would like to quit, type exit.')
        rand_top = ''

for i in range( 0, amount ):
    print('Number ' + str(i + 1) + ':\t' + str(random.randint(1, rand_top)))
    

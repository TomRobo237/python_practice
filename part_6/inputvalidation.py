def validateNumbers():
    while True:
        print('Enter a number: ', end='')
        check = input()
        if check.isdecimal():
            print('It\'s a number alright!')
            break
        else:
            print('Not a number!')
def validateLetters():
    while True:
        print('Enter a password: (Letters and numbers only)')
        check = input()
        if check.isalnum():
            print('Yup, thats fine.')
            break
        else:
            print('Nope, letters and numbers only!')
validateNumbers()
validateLetters()

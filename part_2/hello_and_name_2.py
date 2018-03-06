# Basic Python program to hello world and get some input on the CL.

myname=''
cleanname=''
myage=''

print('Hello World!')
while not myname:
    print('What is your name? ')
    myname = input() # Gathering input and placing into myname
    if myname:
        continue
    else:
        print('Please enter your name!')
print('Nice to meet you, ' + myname)
cleanname=myname.replace(' ','') # Replacing whitespace
print('Your name has ' + str(len(cleanname)) + ' letters.') 

while not myage:
    print('How old are you in years?')
    myage= input()
    try:
        myage=int(myage)
        continue
    except ValueError:
        print('Please enter your age as a whole number!')
        myage=''

if myage <= 10:
    print('Wow, you are young!')
elif myage >= 150:
    print('Nice to see you again, you immortal vampire.')
elif myage >= 60:
    print('Well, are you retired yet?')
else:
    print("You've lived at least " + str(int(myage) * 365) + " Days")

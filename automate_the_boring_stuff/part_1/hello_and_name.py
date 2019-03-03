# Basic Python program to hello world and get some input on the CL.

print('Hello World!')
print('What is your name? ')
myname = input() # Gathering input and placing into myname
# Doesnt handle no value in the variable yet. Will need to work on this.
print('Nice to meet you, ' + myname)
print('The length of your name is: ', end='')
print(len(myname)) #This will include whitespace into the number
print('And your age?')
myage= input()
print("You've lived at least " + str(int(myage) * 365) + " Days")

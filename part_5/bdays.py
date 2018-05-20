import sys
birthdays={'Alice':'Mar 3','Jake':'Apr 13','Percy':'Dec 15'}

while True:
    print('Enter a name: (Blank to quit)')
    name = input()
    if name == '':
        sys.exit()

    if name not in birthdays.keys():
        print('I dont have that person\'s name, What is their birthday?')
        bday_in = input()
        birthdays[name] = bday_in
        print('Birthday database updated.')
    else:
        print( name + '\'s birthday is ' + birthdays[name] )
    

import os
import sys
import json

MyPets = []
MainOpts = ['Check List', 'Add / Remove pet', 'Guess Pets' , 'Exit']
EditOpts = ['Add Pet', 'Remove Pet', 'Return']

def Get_Pets():
    if os.path.isfile(os.path.expanduser('~/pets.txt')):
        if os.stat(os.path.expanduser('~/pets.txt')).st_size == 0:
            print('No Pets to load!')
            return()
        else:
            with open(os.path.expanduser('~/pets.txt'),'r') as file_pointer:
                Pet_list = json.load( file_pointer )
                file_pointer.close()
                return( Pet_list )
    else:
        print('No Pets file!')
        return()
    
def Put_Pets():
    with open(os.path.expanduser('~/pets.txt'), 'w') as file_pointer:
        json.dump(MyPets, file_pointer)
        file_pointer.close()
        
def Number_Check( attempt ):
    try:
        int(attempt)
        return 0
    except ValueError:
        print('Not a valid number!')
        return 1

def Menu( optlist ):
    for num, opt in enumerate(optlist):
        print(str(num+1)+'.', opt)
    while True:
        select = input()
        if Number_Check( select ) == 0:
            if int(select) in  (list(range(1, len(optlist) + 1))):            
                return(int(select))
            else:
                print('Not a valid option\nTry 1-'+ str(len(options)) + '.\nSelection? ')
                select = ''
        else:
            print('Selection? ')

def Print_Pets():
    print('Current Pets:')
    if len(MyPets) == 0:
        print('I have no cats and I must pet.')
    for i in MyPets:
        print ( i )

def Guess_Pets():
    if len(MyPets) == 0:
        print('I have no Pets!')
        return()
    while True:
        print('Enter the name of the pet: ')
        name = input()
        if name in MyPets:
            print(name + ' is a pet in my list!\nTry Again? (Y/N)')
            if Retry() == 0:
                break
        else:
            print(name + ' is not a pet in my list!\nTry Again? (Y/N)')
            if Retry() == 0:
                break

def Retry():
    while True:
        choice = input()
        if choice == 'N' or choice == 'n':
            return 0
        elif choice == 'Y' or choice == 'y':
            return 1
        else:
            print(choice + ' is not Y or N!')
            choice = ''

def Edit_Menu():
    while True:
        print('What would you like to do?')
        choice = Menu( EditOpts )
        if choice == 1:
            print('Pet name?')
            addpet = input()
            MyPets.append( addpet )
            print('Added ' + addpet + ' to list')
        elif choice == 2:
            if len(MyPets) == 0:
                print('I have no Pets!')
            else:
                print('Which would you like to remove?')
                MyPets.remove(MyPets[(Menu( MyPets ) - 1)])
        elif choice == 3:           
            print('Back to main menu...')
            break                

MyPets = list(Get_Pets())
while True:
    print('What would you like to do?')
    choice = Menu( MainOpts )
    if choice == 1:
        Print_Pets()
    elif choice == 2:
        Edit_Menu()
    elif choice == 3:
        Guess_Pets()
    elif choice == 4:
        print('Exiting... Writing pets list.')
        Put_Pets()
        sys.exit()

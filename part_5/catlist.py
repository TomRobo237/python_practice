import sys

MyPets = ['Lina','Zelda','Grace','Serenity']
MainOpts = ['Check List', 'Add / Remove pet', 'Exit']
EditOpts = ['Add Pet', 'Remove Pet', 'Return']

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
    for i in MyPets:
        print ( i )

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
            print('Which would you like to remove?')
            MyPets.remove(MyPets[(Menu( MyPets ) - 1)])
        elif choice == 3:
            print('Back to main menu...')
            break                
while True:
    print('What would you like to do?')
    choice = Menu( MainOpts )
    if choice == 1:
        Print_Pets()
    elif choice == 2:
        Edit_Menu()
    elif choice == 3:
        print('Exiting...')
        sys.exit()

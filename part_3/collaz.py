import sys

def collaz( value ):
    if ( value % 2 ) == 0:
        return ( value // 2)
    else:
        return (( value * 3) + 1 )

def number_check( value ):
    try:
        int( value )
        return 0
    except ValueError:
        print( "Please enter a whole number." )
        return 1
    
while True:
    number=''
    while not number:
        print( "Enter a number: ", end="" )
        number = input()
        if number == 'exit':
            print( "Exiting..." )
            sys.exit()
        elif number_check( number ) == 1:
            number=''
        else:
            number= int( number )
            print( "Collaz value of: " + str( collaz( number ) ) )

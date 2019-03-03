import sys

def collaz( value ):
    if ( value % 2 ) == 0:
        return ( value // 2)
    else:
        return ( ( value * 3) + 1 )

def number_check( value ):
    try:
        int( value )
        return 0
    except ValueError:
        print( "Please enter a whole number." )
        return 1
    
while True:
    number=''
    output=''
    while not number:
        print( "Enter a number: ", end="" )
        number= input()
        if number == 'exit':
            print( "Exiting..." )
            sys.exit()
        elif number_check( number ) == 1:
            number=''
        else:
            number= int( number )
        break
    print( "Collaz sequence for " + str( number ) )
    print ( str( number ), end=" " )
    output = collaz( number )
    print ( str( output ), end=" " )
    while output != 1:
        output = collaz( output )
        print( str( output ), end=" " )
    if output == 1:
        print( end="\n" )
        sys.exit()

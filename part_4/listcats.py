import sys
catnames = [] # Empty array to put names into

print("Enter name of the cat " + str( len( catnames ) + 1 )
    + ": (enter nothing or exit to stop)")
while True:
    name = input()
    if (name == '') or (name == 'exit'):
        if len( catnames ) == 0:
            print( "No names entered!")
            sys.exit()
        break 
    catnames = catnames + [name] # adding to list
    print("Enter name of the cat " + str( len( catnames ) + 1 ) +": "  )
if len( catnames ) == 1:
    print( "The cat's name is: " + catnames[0] )
else:
    print( "The " + str( len( catnames ) ) + " cats' names are:" )
    for name in catnames:
        print( " " + name )

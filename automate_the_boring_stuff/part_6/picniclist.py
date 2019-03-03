#! /usr/bin/env python3
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for i , j in itemsDict.items():
        print(i.ljust(leftWidth, '.') + str(j).rjust(rightWidth))
        

picnicItems = { 'sammiches': 20 , 'apples': 10, 'cups':4 , 'fried beans': 3000 }
printPicnic(picnicItems, 12 , 5)
printPicnic(picnicItems, 20 , 6)

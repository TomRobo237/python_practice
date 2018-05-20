stuff = {'arrow': 12 ,'gold': 42 ,'rope': 1 ,'torch': 6 ,'dagger': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Current items:')
    total_items = 0
    for i in inventory.keys():
        print( str(inventory[i]) +'\t'+ i )
        total_items = total_items + inventory[i]
    print('Total items: ' + str(total_items) )

def addToInventory(inventory, loot):
    print('Added items:')
    for i in loot:
        print( i )
        if i not in inventory:
            inventory[i] = 1
        else:
            inventory[i] = inventory[i] + 1

displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)

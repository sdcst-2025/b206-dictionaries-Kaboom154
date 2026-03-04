#!python3
"""
##### Task 4
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have. You will need to use the string.split() method to separate the command from the item.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""

# looks like the difference from the last one is this will have multiples of items
inventory ={
    'food' : 0,
    'water' : 0,
    'rope' : 0,
    'torch' : 0,
    'sack' : 0,
    'wood' : 0,
    'iron' : 0,
    'steel' : 0,
    'ginger' : 0,
    'garlic' : 0,
    'fish' : 0,
    'stone' : 0,
    'wool' : 0
}


def getItem(item, quantity=1):
    try: 
        int(quantity)
    except:
        print(f'number {quantity} is not a valid input')
    if item not in inventory:
        print(f'item {item} not found in inventory')
    else:
        inventory[item] = inventory[item] + int(quantity)

def dropItem(item, quantity=1):
    try: 
        int(quantity)
    except:
        print(f'{quantity} is not a valid input')
    if item not in inventory:
        print(f'item {item} not found in inventory')
    if inventory[item] < int(quantity):
        print(f'insufficient {item}, only {inventory[item]} {item} was dropped')
        inventory[item] = 0
    else:
        inventory[item] = inventory[item] - int(quantity)

def showInventory():
    count = 0
    print('You have:')
    for i in inventory:
        if inventory[i] > 0:
            print(f' {inventory[i]} {i}')
        else:
            count += 1
    if count == len(inventory):
        print(' nothing')

def start():
    while True:
        command = input('enter command:  ').split(' ', 2)
        if 'get' in command[0] or 'g' in command[0]:
            if len(command) == 1:
                print('an item to be gotten up must be specified')
            elif len(command) == 2:
                getItem(command[1])
            else:
                getItem(command[2],command[1])
        elif 'drop' in command[0] or 'dr' in command[0]:
            if len(command) == 1:
                print('an item to be dropped must be specified')
            elif len(command) == 2:
                dropItem(command[1])
            else: 
                dropItem(command[2],command[1])
        elif 'inventory' in command[0] or 'inv' in command[0]:
            showInventory()
        elif 'end' in command[0]:
            break

start()
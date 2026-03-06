'''
Task 4
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to 'drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have. You will need to make use of the string.split() method in order to separate the item name from the action that precedes it.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)
'''

#cmds:
#get -- aliases: g
#drop -- aliases: dr, d
#show inventory -- aliases: sh, inv,

inventory = {
    'longsword' : 'a longer sword',
    'plate mail' : 'made of the finest china'
}

def getItem(itemName, itemStats=''):
    inventory[itemName] = itemStats
    #start()

def dropItem(itemName):
    try:
        del inventory[itemName]
    except:
        print(f'no item {itemName} found')
    #start()

def showInventory():
    print('------------------------------')
    for i in inventory:
        print(f'{i}  --  {inventory[i]}')
    print('------------------------------')
    #start()

def help():
    print('-----------------------')
    print('commands:')
    print('''
        get        --  give yourself an item             --  aliases: get, g
        drop       --  drop an item from your inventory  --  aliases: drop, dr
        inventory  --  displays your current inventory   --  aliases: inventory, inv
        end        --  quit the program
    ''')
    print('-----------------------')
    #start()

def start():
    while True:
        command = input('enter command:  ').split(' ', 2)
        if 'help' in command[0]:
            help()
        elif 'get' in command[0] or 'g' in command[0]:
            if command[1] == '':
                print('an item to be gotten up must be specified')
            else:
                getItem(command[1],command[2])
        elif 'drop' in command[0] or 'dr' in command[0]:
            if command[1] == '':
                print('an item to be dropped must be specified')
            else: 
                dropItem(command[1])
        elif 'inventory' in command[0] or 'inv' in command[0]:
            showInventory()
        elif 'end' in command[0]:
            break

start()

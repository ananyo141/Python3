# Create a fantasy videogame inventory model where function displayInventory() will print the stuff
# present and addToInventory() adds loot items to inventory.
import sys

def displayInventory(playerInventory):
    '''(dict)-->NoneType
    Display the current contents of the dict playerInventory with the quantities of each and the total.
    '''
    total=0
    print("INVENTORY".center(20, '-'))
    for key, value in playerInventory.items():
        print(str(key).ljust(10)+" : "+str(value).rjust(10))
    for value in playerInventory.values():
        total+=value
    print("Total items present in inventory is:",total)

def addToInventory(lootBox,playerInventory):
    '''(list,dict)-->NoneType
    Modify the playerInventory to add the lootBox items(keys and values) to it.
    '''
    for item in lootBox:
        playerInventory.setdefault(item,0)
        playerInventory[item]=playerInventory[item]+1
    
def main():
    playerInventory = {}
    playerInventoryDefault = {'rope': 1, 'torch': 6,
                          'gold coin': 42, 'dagger': 1, 'arrow': 12}


    # Wanted to create a function out of this, but the first one creates a dict and the other list.
    print("Do you wish to add you own inventory or use default from source code?")
    inventoryChoice = input("('Enter' to use yours else 'default'): ")
    if inventoryChoice.lower()=="enter":
        item=input("Enter the item you want to add(Done to exit): ")
        while item.lower()!='done':
            try:
                playerInventory[item]=int(input("Enter the quantity: "))
            except:
                sys.exit("Invalid Input")
            item = input("Enter the item you want to add(Done to exit): ")
    elif inventoryChoice.lower()=="default":
        playerInventory=playerInventoryDefault
    else:
        sys.exit("You entered a wrong choice")

    displayInventory(playerInventory)

    lootChoice = input("Do you want to add items from the lootBox?(Y/N): ")
    # Make the list of items for lootbox.
    crate=[]
    if lootChoice.lower()=='y':
        item=input("Enter crate item('Done' to finish): ")
        while item.lower()!='done':
            crate.append(item)
            item = input("Enter crate item('Done' to finish): ")
    elif lootChoice.lower()=='n':
        print("You chose not to enter anything to inventory.\nFinal inventory:")
        displayInventory(playerInventory)
        sys.exit()
    else:
        sys.exit("What you entered wasn't a valid choice. Try again.")
    
    addToInventory(crate,playerInventory)
    print("Updated inventory: ")
    displayInventory(playerInventory)
    
if __name__=="__main__":
    main()





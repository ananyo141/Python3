# WAP that gets what the guests are bringing for a picnic using a dictionary data structure.
import os

def clearScreen():
    '''(NoneType)-->NoneType
    Clear the console screen.
    '''
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def returnItems(allGuests):
    '''(dict of dicts)-->dict
    Return all the items brought by the guests and tally the total number of the items from all guests.
    '''
    items={}
    # Making a new dict that tracks and tallies only the items taken in.
    for guests in allGuests:
        for itemName,quantity in allGuests[guests].items():
            items.setdefault(itemName,0)
            items[itemName]=items[itemName]+quantity
    return items

def printItems(itemsDict,tableTitle,leftWidth,rightWidth):
    '''(dict)-->NoneType
    Print the item keys and their values in the given items dictionary in a tabular form.
    '''
    # Take the given dict and value and print it in table according to width specified as argument while calling.
    print(tableTitle.center(leftWidth+rightWidth,'-'))
    for keys,values in itemsDict.items():
        print(keys.ljust(leftWidth,'.')+str(values).rjust(rightWidth))

# guestContribution is a dict of dict that takes in guest names(str) as keys and assigns to each name
# a dict, containing item name as key and it's quantity as value.
guestContribution={}
name=input("Enter name of the guest('done' to exit): ")
while name!='done':
    allItems={}
    item=input("Enter the item name(return to exit): ")
    while item!='':
        quantity=int(input("Enter the quantity: "))
        allItems[item]=quantity
        item = input("Enter the item name(return to exit): ")
    guestContribution[name]=allItems
    name = input("Enter name of the guest('done' to exit): ")



clearScreen()
itemTotal=returnItems(guestContribution)
printItems(itemTotal,'Picnic Items',20,6)
print("\n\nContributed by: (Don't give apple pie to the ones who didn't pitch in)")
printItems(guestContribution,'Guests',10,6)

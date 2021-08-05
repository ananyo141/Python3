#WAP to import a list of numbers from the user, display it, 
#then prompt the user to shift to right or left with the help of 'shiftToRight' and 'shiftToLeft' module.

from shiftToRight import shiftToRight
from shiftToLeft import shiftToLeft


list1=[]
asking=input("Please enter the number to add to list: ")
while asking!='done':
    try:
        list1.append(int(asking))
        asking=input("Enter 'done' to stop adding; else continue.\n")
    except:
        asking=input("Please enter a valid number. Error adding to list.\n")
        continue

print("\n\nThe entered list of numbers is",list1)
choice=input("\nEnter 'shift to right' or 'shift to left' or 'both' to commence the respective action.\n")
if choice=='shift to right':
    print("\nCommencing shift to right")
    shiftToRight(list1)
    print("\nShifting completed. Modified list is:",list1)
elif choice=='shift to left':
    print("\nCommencing shift to left")
    shiftToLeft(list1)
    print("\nShifting completed. Modified list is:",list1)
elif choice=='both':
    print("\nCommencing shift to right")
    shiftToRight(list1)
    print("\nShifting completed. Modified list is:",list1)
    print("\nCommencing shift to left")
    shiftToLeft(list1)
    shiftToLeft(list1)
    print("\nShifting completed. Modified list is:",list1)
else:
    print("You didn't enter a valid choice. Process terminated.")


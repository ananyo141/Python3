# Make a sandwich maker and display the cost.
import pyinputplus as pyip
orderPrice = 0

print("Welcome to Python Sandwich!".center(100,'*'))
print("We'll take your order soon.\n")

breadType = pyip.inputMenu(['wheat','white','sourdough'],prompt="How do you like your bread?\n",blank=True)
if breadType:
    orderPrice += 20
proteinType = pyip.inputMenu(['chicken','turkey','ham','tofu'],prompt="\nWhat is your protein preference?\n",blank=True)
if proteinType:
    orderPrice += 35
cheese = pyip.inputYesNo(prompt = '\nDo you prefer cheese?: ')
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar','Swiss','mozarella'],prompt="Enter cheese type: ")
    orderPrice += 10

mayo = pyip.inputYesNo(prompt='\nDo you want mayo?: ')
if mayo == 'yes':
    orderPrice += 5
mustard = pyip.inputYesNo(prompt='\nDo you want to add mustard?: ')
if mustard == 'yes':
    orderPrice += 2
lettuce = pyip.inputYesNo(prompt='\nDo you want lettuce?: ')
tomato = pyip.inputYesNo(prompt='\nDo you want tomato in your sandwich?: ')
orderQuantity = pyip.inputInt('\nHow many sandwiches do you want to order?: ',min=1)
confirmation  = pyip.inputYesNo(prompt='\nConfirm your order?: ')
if confirmation == 'yes':
    totalOrderPrice = orderPrice * orderQuantity
    print(f"\nYour order has been confirmed! Total order price is Rs.{totalOrderPrice} for {orderQuantity} sandwiches.")
else:
    print('\nYou cancelled your order')



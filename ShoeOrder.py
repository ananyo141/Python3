#There are 955 shoes left in a Nike store. WAP for the customer to find out if the number of shoes
# needed he can get from the store, prompt if he wants to place, and deduct from total if he orders.
print("Hi there! Welcome to the official NIKE Outlet. We currently have 955 shoes in our stocks, check if your needs can be met by using the function checkAvailability(order_quantity)")
def checkAvailability(order_quantity):
    '''(num)--->num
Check if the input order quantity is available to purchase, and place order if the user wants to buy, return the order quantity.
>>>checkAvailability(345)
Your order is available. Do you want to place your order? Y/N
Y
Thank you for shopping with us! Your Nike order details: 345 shoes
Units left: 610
345
'''
    available_units=955
    if order_quantity <= available_units:
        prompt=input("Your order is available. Do you want to place your order? Y/N\n")
        if prompt == 'Y':
            available_units-= order_quantity
            print("Thank you for shopping with us! Your Nike order details:",order_quantity,"shoes")
            print("Units left:", available_units)
            return order_quantity
        elif prompt== 'N':
            print("You cancelled the purchase!")
        else:
            print("You entered something other than Y or N. Sorry!")
    else:
         print("Sorry, due to high demand, stocks are limited. Please try again later.")
            

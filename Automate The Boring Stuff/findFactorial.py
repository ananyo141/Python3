# WAP to find the factorial of a given number.

def factorial(number):
    '''(int)-int
    Return the factorial of the given number.
    >>>factorial(6)
    720
    '''
    value=1
    i=number
    while(i!=1):
        value*=i
        i-=1
    return value


num=input("Enter the number you want to find the factorial of: ")
try:
    numVal=int(num)
except:
    print("Invalid Input")
print("The required factorial of the input number is", factorial(numVal))
    

# Find the phone number in the given string without the help of regex.
import time

def isAmrPhNum(string):
    '''(str)-->Bool
    Return boolean True/False according to if the given string corresponds to an American phone number.
    Precondition: The entered phone number should be of the format: 415-555-4242
    '''
    if len(string) != 12:
        return False
    if not string[0:3].isdecimal():
        return False
    if string[3] != '-' or string[7] != '-':
        return False
    if not string[4:7].isdecimal():
        return False
    if not string[8:12].isdecimal():
        return False
    return True

def isInPhnNum(string):
    '''(str)-->Bool
    Return boolean True/False according to if the given string corresponds to an Indian phone number.
    Precondition: The entered phone number should be of the format: (+91)7593-548298
    '''
    if len(string) != 16:
        return False
    if string[0] != '(' or string[1] != '+' or string[4] != ')' or string[9] != '-':
        return False
    if not string[2:4].isdecimal():
        return False
    if not string[5:9].isdecimal():
        return False
    if not string[10:16].isdecimal():
        return False
    return True

def main():
    choice = input("Do you want to search for Indian phone numbers or American phone numbers?: ")
    inputString = input("Enter the string you want to analyze for numbers:\n")
    if choice.lower().startswith('india'):
        print("Searching for Indian phone numbers")
        time.sleep(0.5)
        for i in range(len(inputString)):
            message = inputString[i:i+16]
            if isInPhnNum(message):
                print("Indian Phone Number found:",message)
    
    elif choice.lower().startswith('america'):
        print("Searching for American phone numbers")
        time.sleep(0.5)
        for i in range(len(inputString)):
            message = inputString[i:i+12]
            if isAmrPhNum(message):
                print("American Phone Number found:",message)

    else:
        print("Matching numbers couldn't be found")

if __name__ == '__main__':
    main()

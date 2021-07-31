# Find phone numbers in the text input by user with the help of regex.
import re, time, sys

# Regex for American phone numbers
def isAmrPhNum(string):
    '''(str)-->Bool
    Return boolean True/False according to if the given string corresponds to an American phone number.
    Precondition: The entered phone number should be of the format: 415-555-4242
    '''
    americanNum = re.compile(r'\d{3}\-\d{3}\-\d{4}')
    foundNumbers = americanNum.findall(string)
    return foundNumbers

# Regex for Indian phone numbers
def isInPhnNum(string):
    '''(str)-->Bool
    Return boolean True/False according to if the given string corresponds to an Indian phone number.
    Precondition: The entered phone number should be of the format: (+91)7593-548298
    '''
    indianNum = re.compile(r'\(\+\d{2}\)\d{4}\-\d{6}')
    foundNumbers = indianNum.findall(string)
    return foundNumbers


def main():
    choice = input("Do you want to search for Indian phone numbers or American phone numbers?: ")
    inputString = input("Enter the string you want to analyze for numbers:\n")
    
    if choice.lower().startswith('india'):
        findingNumOf = 'Indian'
        print("Searching for", findingNumOf, "phone numbers")
        findNumbers = isInPhnNum(inputString)

    elif choice.lower().startswith('america'):
        findingNumOf = 'American'
        print("Searching for", findingNumOf, "phone numbers")
        findNumbers = isAmrPhNum(inputString)
    
    else:
        sys.exit("Matching numbers couldn't be found")

    time.sleep(0.5)
    if len(findNumbers) < 1:
        sys.exit("Matching numbers couldn't be found")

    for number in findNumbers:
        print(findingNumOf,"Number found:", number)
    print("Done")


if __name__ == '__main__':
    main()

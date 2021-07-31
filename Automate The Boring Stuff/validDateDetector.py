#!python3
# Write regex that detects dates in a given string and check if the dates are valid or not.
import re, pyperclip, random, time, sys

def dateFinder(text):
    '''(str)--->list of list
    Return the dd/mm/yyyy in a list of list found in the given text.
    '''

    # Starting with year(\d{4}), so first year is matched or (\d{1,2}) will try to match date first,
    # taking year's two digits and it's value is lost.
    dateRegex = re.compile(r'''(
        ((\d{4})|(\d{1,2}))          # First part either date or year
        (/|\.|-)                     # separator
        (\d{1,2})                    # month
        (/|\.|-)                     # separator
        ((\d{4})|(\d{1,2}))          # either date or year
    )''', re.VERBOSE)

    datesFound = []
    for tupleGroup in dateRegex.findall(text):
        dateList = []
        dateList.append(int(tupleGroup[3]+tupleGroup[9]))      # date
        dateList.append(int(tupleGroup[5]))                    # month
        dateList.append(int(tupleGroup[2]+tupleGroup[8]))      # year

        datesFound.append(dateList)

    return datesFound

def dateValidator(date,month,year):
    '''(int,int,int) ---> bool
    Return boolean True/False according to if the date entered is valid.
    '''
    monthsWith30Days = [4,6,11]
    validation = True

    # Remove invalid dates
    if year<1000 or year>2999:
        validation = False
    elif  month<1 or month>12:
        validation = False
    elif date<1 or date>31:
        validation = False

    # Find matching dates for 30 and 31 dates according to month
    elif (month in monthsWith30Days) and date>30:
        validation = False
    elif (month !=2 and (month not in monthsWith30Days)) and date>31:
        validation = False

    # Special case for February
    elif month == 2:
        # Find if leap year
        isLeapYear = False
        if year%4 == 0 and year%100 != 0:
            isLeapYear = True
        elif year%100 == 0 and year%400 == 0:
            isLeapYear = True
        # Assign date limit according to Leap year or not
        if isLeapYear:
            if date>29:
                validation = False
        else:
            if date>28:
                validation = False
    return validation

# Use sys argv to give option to user to either enter dates or find from clipboard
def main():
    if len(sys.argv)<2:
        sys.exit("Please specify the mode when executing script {enter, clipboard, random}")
    choice = sys.argv[1]
    
    if choice.lower().startswith("clip"):
        clipboard = pyperclip.paste()
        datesInClip = dateFinder(clipboard)
        for date, month, year in datesInClip:
            if dateValidator(date,month,year) == True:
                print(f"{date}/{month}/{year} is valid.")
            else:
                print(f"{date}/{month}/{year} is invalid.")

    elif choice.lower().startswith("enter"):
        dateInput = input("Enter the date you want to verify:(dd/mm/yyyy) ")
        try:
            date = int(dateInput[0:2])
            month = int(dateInput[3:5])
            year = int(dateInput[6:10])
        except ValueError:
            sys.exit("Enter correct date to check dumbass")

        if dateValidator(date, month, year) == True:
            print(f"{date}/{month}/{year} is valid.")
        else:
            print(f"{date}/{month}/{year} is invalid.")

    elif choice.lower() == 'random':
        try:
            while True:
                date = random.randint(1, 31)
                month = random.randint(1, 12)
                year = random.randint(1000, 2999)

                if dateValidator(date, month, year):
                    print(f"Valid date generated: {date}/{month}/{year}")
                    time.sleep(0.1)
                else:
                    print(f"Invalid date generated: {date}/{month}/{year}")
                    time.sleep(0.25)
        except KeyboardInterrupt:
            sys.exit("\nThanks for being silly with me!")

   
if __name__ == '__main__':
    main()
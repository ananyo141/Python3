#! python3
# Clean the dates in the clipboard by substituting in the given text in a standard format with the help of regex.
import re
from ModuleImporter import module_importer
pyperclip = module_importer('pyperclip', 'pyperclip')

def dateCleaner(string):
    '''(str)-->str
    Substitute the dates given in the string with a cleaner and standard format of the dates.
    '''
    # Create date Regex:
    dateRegex = re.compile(r'''(
        ((\d{4}) | (\d{1,2}))      # First digit either date or year
        (/|-|\.)                   # Separator
        (\d{1,2})                  # Second digit (month)
        (/|-|\.)                   # Separator
        ((\d{4}) | (\d{1,2}))      # Last digit either date or year
        )''', re.VERBOSE)

    # Groups in sub() and findall() work differently, findall() starts with 0 and sub() with 1 #
    # Grouping Algorithm:
    # To display in a standardized format, the first group to be displayed should be the date group number,
    # (here either 3 in findall or 4 in sub), the month (5 in findall or 6 in sub), and finally the
    # year group (8 in findall or 9 in sub).

    # With findall() method, this will return a list.
    # cleanedDates = []
    # for tupleGroup in dateRegex.findall(string):
    #     cleanedDates.append(tupleGroup[3]+tupleGroup[9]+'/'+tupleGroup[5]+'/'+tupleGroup[2]+tupleGroup[8])

    cleanedDates = dateRegex.sub(r"\4\10/\6/\3\9",string)   # This raw string 'r' is hella important

    return cleanedDates


def main():
    clipboard = pyperclip.paste()
    cleanClipboard = dateCleaner(clipboard)
    if len(cleanClipboard) > 0:
        successNotice = "Dates found and successfully cleaned"
        pyperclip.copy(successNotice.center(len(successNotice)+10,'-') + '\n' + cleanClipboard)
        print("Clipboard successfully cleaned")
    else:
        print("No dates found")

if __name__ == '__main__':
    main()

    
      

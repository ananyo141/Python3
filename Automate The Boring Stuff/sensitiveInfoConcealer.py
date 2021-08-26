# Remove the sensitive information like credit cards, social security numbers, phone numbers from the clipboard.
import re
from ModuleImporter import module_importer
pyperclip = module_importer('pyperclip', 'pyperclip')

def infoConcealer(text):
    '''(str)-->str
    Return a modified text where any matching sensitive information is ommitted.
    '''
    # Regex string for credit card numbers
    cardRegex = '''(
        (\d{4})          # First 4 Digits
        (\s* | -)?       # Optional Separator   
        (\d{4})          # Second 4 Digits
        (\s* | -)?       # Optional Separator   
        (\d{4})          # Third 4 Digits
        (\s* | -)?       # Optional Separator
        (\d{4})          # Last 4 Digits
        )'''
    
    # Regex string for social security numbers.
    socialSecurityRegex = '''(
        (\d{3})          # First 3 digits           
        (\s* | -)        # Separator
        (\d{2})          # Second 2 digits
        (\s* | -)        # Separator
        (\d{4})          # Last 4 digits
        )'''
    
    # Regex string for phone numbers
    phoneNumberRegex = '''(
        ((\+)?91)?       # Area code
        (\s*|-)?         # Optional Separator
        (\d{5})          # First 5 digits
        (\s*|-)?         # Optional Separator
        (\d{5})          # Last 5 digits
        )'''

    combinedRegex = re.compile(fr'{cardRegex} | {socialSecurityRegex} | {phoneNumberRegex}', re.VERBOSE)
    subText = combinedRegex.sub('****', text)
    return subText

def main():
    clipboard = pyperclip.paste()
    newClipboard = infoConcealer(clipboard)
    pyperclip.copy(newClipboard)
    print("Info Concealed")

if __name__ == '__main__':
    main()

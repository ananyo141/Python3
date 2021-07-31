#! python3
# This script uses regex to extract phone, email, from clipboard.

import pyperclip
from functions import *

def main():
    clipboard = pyperclip.paste()
    stringToCopy = ''

    # Find the phone numbers in clipboard contents
    phoneNumbers = findPhoneNumbers(clipboard)
    if len(phoneNumbers) >= 1:
        stringToCopy += 'Phone Numbers Found'.center(30,'-') + '\n'
        for item in phoneNumbers:
            stringToCopy += item + '\n'
        stringToCopy += '\n'

    # Find the email addresses in clipboard contents
    emails = findEmailAddr(clipboard)
    if len(emails) >= 1:
        stringToCopy += 'Email Addresses Found'.center(30, '-') + '\n'
        for item in emails:
            stringToCopy += item + '\n'
        stringToCopy += '\n'

    # Find the website URLs in clipboard contents
    websites = findWebsites(clipboard)
    if len(websites) >= 1:
        stringToCopy += 'Websites Found'.center(30, '-') + '\n'
        for item in websites:
            stringToCopy += item + '\n'

    # Finally, copy matched contents in clipboard
    pyperclip.copy(stringToCopy)
    print("data extraction completed successfully (100%)...".title())


if __name__ == '__main__':
    main()


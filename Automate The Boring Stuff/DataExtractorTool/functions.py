import re

# Regex to find the phone numbers
def findPhoneNumbers(string):
    '''(str)-->list
    Return all the matching phone numbers in the given string as a list.
    '''
    phoneNumbersIN = re.compile(r'''(           # Indian phone numbers (+91)9590320525
        ( ((\+)?\d{2}) | \(((\+)?\d{2})\) )?    # (+91) parenthesis and + optional or whole is optional, but if present area code 91 is mandatory
        ( \s* |-| \. )?                          # optional separator
        (\d{5})
        ( \s*|-|\. )?                            # optional separator
        (\d{5})
        )''', re.VERBOSE)

    phoneNumbersAmer = re.compile(r'''(
        ( \d{3} | \( \d{3} \) )?                # area code
        (\s |-| \.)?                            # optional separator
        (\d{3})                                 # first 3 digits
        (\s |-| \.)                             # required separator
        (\d{4})                                 # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?          # optional extension
        )''', re.VERBOSE)
        
    # Find the numbers and return them in a list container
    numbers = []

    indianNum = []
    indianNum.append("Indian Numbers:")
    for tupleGroup in phoneNumbersIN.findall(string):       # findall() returns tuples of regex group strings
        numberFound = '(+91) '+tupleGroup[7]+'-'+tupleGroup[9]
        if len(numberFound) >= 17:
            indianNum.append(numberFound)
    if len(indianNum) > 1:
        numbers.extend(indianNum)

    amerNum = []
    amerNum.append("American Numbers:")
    for tupleGroup in phoneNumbersAmer.findall(string):
        phoneNum = '-'.join([tupleGroup[1],tupleGroup[3],tupleGroup[5]])
        if tupleGroup[8] != '':
            phoneNum += ' x' + tupleGroup[8]       # 8 can only be justified if nested group is counted separatedly,index starting from the outer group
        if len(phoneNum) >= 12:
            amerNum.append(phoneNum)
    if len(amerNum) > 1:
        numbers.extend(amerNum)

    return numbers

# Regex to find email addresses
def findEmailAddr(string):
    '''(str)-->list
    Return all the matching email addresses in the given string as a list.
    '''
    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # one or more of the characters defined in the class (username)
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # one or more of the characters defined in the class (domain name)
    (\.[a-zA-Z]{2,4})           # dot-something
    )''', re.VERBOSE | re.IGNORECASE)
    
    emailMatch = []
    for tupleGroup in emailRegex.findall(string):
        emailMatch.append(tupleGroup[0].lower())            # FLAGGED #

    return emailMatch

# Regex to find website URL
def findWebsites(string):
    '''(str)-->list
    Return a list of matching websites found in the given string.
    '''
    websiteRegex = re.compile(r'''(
        ( http:// | https:// )?     # optional protocol
        (www\.)                     # prefix
        [a-z0-9.$-_. +! *'()]+      # host name
        (\.)                        # period
        ([a-z]{2,4})                # top-level domain name
        (\.)?                       # optional domains
        ([a-z]{2,4})?
        (\.)?
        ([a-z]{2,4})?
        )''', re.VERBOSE | re.IGNORECASE)

    websitesMatch = []
    for tupleGroup in websiteRegex.findall(string):
        formatter = tupleGroup[0].lstrip('https://www./')
        websitesMatch.append(('www.'+formatter).lower())

    return websitesMatch



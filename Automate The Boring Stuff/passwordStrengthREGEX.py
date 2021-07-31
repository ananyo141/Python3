# Find if the entered password is strong.
import re

def passwordStrength(passw):
    '''(str)--->bool
    Return boolean T according to if the password passed is strong, None if weak.
    '''
    # Regex password strength
    characterRegex = re.compile(r'''(
    ([A-Z]+)  # capital and lower
    ([a-z]+)
    (\d+)
    )''',re.VERBOSE)

    lengthRegex = re.compile(r'.{8,}')
    lengthMatch = lengthRegex.search(passw)
    charMatch = characterRegex.search(passw)

    if lengthMatch and charMatch:
        return True


def main():
    password = input("Enter the password you want to evaluate: ")
    ifStrong = passwordStrength(password)
    if ifStrong:
        print("Strong")
    else:
        print("Weak")

if __name__ == '__main__':
    main()

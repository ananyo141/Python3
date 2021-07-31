# Give the user option to find the passwords in the given text, or enter one manually.
# Check the password and give rating as weak, medium, strong, unbreakable and include tips to improve it.
import re, pyperclip, time, sys

def passwordFinder(text):
    '''(str)--->list
    Find and return matching password strings in the given text.
    '''
    passwordRegex = re.compile(r'''(
        (password | pass)       # Starts with 'password'
        (?: : | -)?             # optional separator 
        (?: \s*)?               # Optional whitespaces        
        (\S{3,})                # Atleast 3 non-space characters
    )''', re.VERBOSE | re.IGNORECASE)

    passwordsFound = []
    for tupleGroup in passwordRegex.findall(text):
        passwordsFound.append(tupleGroup[2])

    return passwordsFound

def passwordStrength(passw):
    '''(str)--->NoneType
    Print the strength of the given password between weak, medium, strong and unbreakable along with 
    tips to strengthen the password.
    '''
    specialCharRegex = re.compile(r'[!@#$%^&*-+]')
    characterCheck = uppercaseCheck = lowercaseCheck = digitCheck = specialCharCheck = False
    strengthScore = 0

    if len(passw) >= 8:
        characterCheck = True
        strengthScore += 1
    # Find uppercase
    for char in passw:
        if char.isupper():
            uppercaseCheck = True
            strengthScore += 1
            break
    # Find lowercase
    for char in passw:
        if char.islower():
            lowercaseCheck = True
            strengthScore += 1
            break
    # Find digit
    for char in passw:
        if char.isdecimal():
            digitCheck = True
            strengthScore += 1
            break
    # Find special Character
    specialChar = specialCharRegex.search(passw)
    if specialChar:
        specialCharCheck = True
        strengthScore += 1

    # Score strength
    if strengthScore == 5:
        print("Unbreakable\nYou can challenge a hacker!")
    elif strengthScore == 4:
        print("Strong")
    elif strengthScore == 3:
        print("Medium")
    elif strengthScore < 3:
        print("Weak")

    # Add tips to strengthen the password
    if not characterCheck:
        print("Password length is too short")
    if not uppercaseCheck:
        print("Tip: Add an uppercase letter.")
    if not lowercaseCheck:
        print("Tip: Add a lowercase letter.")
    if not digitCheck:
        print("Tip: Add a digit.")
    if not specialCharCheck:
        print("Tip: Add a special character.")


def main():
    if len(sys.argv)>1:
        if sys.argv[1].lower().startswith('clip'):
            clipboard = pyperclip.paste()
            passwords = passwordFinder(clipboard)
            if  len(passwords) == 0:
                sys.exit("No passwords found")

            print("Analyzing".ljust(20,'.'))
            time.sleep(1)
            for i in range(len(passwords)):
                print("\nPassword found:", passwords[i])
                passwordStrength(passwords[i])
                time.sleep(0.25)
            sys.exit("\nThanks for trying this out!")
        else:
            sys.exit("Enter 'clip' during script execution {python <filename>.py clip}\nto find and analyze passwords from your clipboard.")

    password = input("Enter the password: ")
    if ' ' in password:
        sys.exit("Passwords can't contain spaces. Invalid.")
    print("Analyzing......")
    time.sleep(0.5)
    passwordStrength(password) 

    # Usage Reminder
    print('''\nYou can also enter 'clip' during script execution {python <filename>.py clip}
to find and analyze passwords from your clipboard.''')

if __name__ == '__main__':
    main()
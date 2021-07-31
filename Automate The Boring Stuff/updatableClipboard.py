#! python3
# Write a similar multiclipboard program that uses command prompt arguments 
# with save, list and delete functionality

import shelve, pyperclip, sys
keyData = shelve.open('keydataSaveFile')

if len(sys.argv) < 2:
    sys.exit("Usage: Enter filename along with keyword to copy in terminal")

if sys.argv[1].lower() == 'save':
    keyData[sys.argv[2]] = pyperclip.paste()
    sys.exit("The keyword is successfully created")

elif sys.argv[1].lower() == 'list':
    print(list(keyData.keys()))
    sys.exit()

elif sys.argv[1].lower() == 'delete':
    if sys.argv[2].lower() == '-all':
        keyData.clear()
    else:
        del keyData[sys.argv[2]]
elif sys.argv[1].lower() == 'commands':
    print("Commands".center(25))
    print("save".ljust(20) + "save the clipboard under the next given keyword argument")
    print("list".ljust(20) + "list the avaiable keywords to copy")
    print("delete".ljust(20) + "delete the given keyword")
    print("delete -all".ljust(20) + "delete all the keywords and associated values")
    sys.exit()
else:
    pyperclip.copy(keyData.get(sys.argv[1],'No Match'))

keyData.close()
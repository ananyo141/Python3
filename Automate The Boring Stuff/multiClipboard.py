#!python3 
# Write a multiclipboard program that keeps takes a keyword as cmd/terminal argument and copies 
# elaborated text into the clipboard.

import sys,pyperclip,pprint

clipboard = {'absolutely': "Yes! I'm excited for it!",
 'agree': "Yeah I completely agree with you! Let's do this!",
 'disagree': 'I strongly disagree with your opinion.',
 'later': 'Sorry, can we do this later this week?',
 'no': "I think I'm gonna pass. You guys go ahead."}

#Marker: Start second part from here.
if len(sys.argv)<2:
    sys.exit("Usage: python3 [filename.py] [keyword]")

keyword=sys.argv[1]
if keyword in clipboard:
    pyperclip.copy(clipboard[keyword])
    sys.exit("Message successfully copied to clipboard.")

print("No matches!")
choice=input("Do you want to add the message to database?(Y/N): ")

# Records the new string.
if choice.lower()=='y':
    clipboard[keyword] =input("Enter the message you want to add: ")
    updatedClipboard=pprint.pformat(clipboard)

    # Save to source file in 2 parts, one before clipboard and one after.
    fileRead=open("multiClipboard.py",mode='r')
    contentsP1List=[]
    line = fileRead.readline()
    while line.startswith("clipboard") == False:
        contentsP1List.append(line)
        line = fileRead.readline()
    while line!='\n':
        line = fileRead.readline()
    contentsP2 = fileRead.read()
    fileRead.close

    fileWrite=open("multiClipboard.py",mode='w')
    for lines1 in contentsP1List:
        fileWrite.write(lines1)
    fileWrite.write(f"clipboard = {updatedClipboard}")
    fileWrite.write("\n\n")
    fileWrite.write(contentsP2)
    fileWrite.close()

    print("Process successfully completed.")
elif choice.lower()=='n':
    sys.exit("You chose not to add.")

else:
    sys.exit("Invalid choice")
    


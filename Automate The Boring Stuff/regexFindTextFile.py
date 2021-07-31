# Open all .txt file in a folder
# Search for a user supplied regex
# Print result on screen

import tkinter.filedialog, re, os
from pathlib import Path

# Input Folder from user
print("Enter the folder you want to search")
searchFolder = Path(tkinter.filedialog.askdirectory())

# Input regex to search from user
regex = input("Enter Regular Expression to search for: ")
searchRegex = re.compile(fr'{regex}')

# search each .txt file in the given directory
for fileName in searchFolder.glob('*.txt'):
    file = open(fileName, 'r')
    fileContents = file.read()
    for matches in searchRegex.findall(fileContents):
        print(f"Match Found at {os.path.relpath(fileName,(Path.cwd() / Path('..')))}: {matches}")
    file.close()
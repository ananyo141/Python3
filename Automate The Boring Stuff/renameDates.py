#!python3
# # Walk the provided directory for all the filenames in directory and subdirectory 
# to search for filenames with american dates and rename them with European dates.
# MM-DD-YYYY to DD-MM-YYYY

import tkinter.filedialog, shutil, random, re, os
from pathlib import Path
import pyinputplus as pyip

dateRegex = re.compile(r'''(
    ((?: 0?[1-9])|10|11|12)     # month
    (-|/)                       # separator
    ( (?: 0|1|2)?\d|30|31 )     # date
    (-|/)                       # separator
    ((?: 20|19)\d\d)            # year   
    )''', re.VERBOSE)

def dummyFileMaker(directory, fileNum):
    for i in range(fileNum):
        date = random.randint(1,31)
        month = random.randint(1,12)
        year = random.randint(1995, 2025)
        file = open(f'{directory}{os.sep}Dated {month}-{date}-{year}.txt', 'w')
        file.write(f"This is {i+1} number file")
        file.close()

def main():
    # Give the user choice to create dummy files to check program usability
    choice = pyip.inputYesNo(prompt="Do you want to use test files to test the program? ")
    if choice == 'yes':
        dummyFileDir = tkinter.filedialog.askdirectory()
        fileNumber = pyip.inputInt(prompt="Enter how many files you want to create: ")
        dummyFileMaker(dummyFileDir, fileNumber)
    else:
        print("No dummy files were created")

    # Main program
    print("Enter the directory you want to crawl for American Dates:")
    enterDir = tkinter.filedialog.askdirectory()

    if enterDir:
        for directory, subdirectory, files in os.walk(enterDir):
            for file in files:
                fileName = str(Path(file).name)
                if dateRegex.search(fileName):
                    newFileName = dateRegex.sub(r'\4-\2-\6', fileName)
                    shutil.move(Path(directory)/fileName , Path(directory)/newFileName)
        print("The files in the directory were renamed successfully")

    else:
        print("User terminated the program")

if __name__ == '__main__':
    main()
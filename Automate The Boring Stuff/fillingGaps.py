#!python3
# This program searches for gaps in numbering in files with a given prefix in directory

import tkinter.filedialog, shutil, sys, os
import pyinputplus as pyip
from pathlib import Path

# Input insert value in terminal for inserting gap in file numbering

def main():
    # Take the prefix to search the directory
    prefix = pyip.inputStr(prompt = "Enter the prefix of your files: ")
    # Take the directory to search
    print("Choose the directory you want to check")
    while True:
        dirChoice = tkinter.filedialog.askdirectory()
        if dirChoice:
            break
    
    toChange = []
    # search the directory for items with the supplied prefix and save to list
    for item in Path(dirChoice).glob(f'{prefix}*'):
        toChange.append(item)    

    # sort the list according to numbering
    sortList = []   # temp list
    sortDict = {}   # temp dict

    for item in toChange:
        numbering = int(Path(item).stem.strip(prefix))
        sortDict[numbering] = item
    for numbers in sortDict.keys():
        sortList.append(numbers)

    sortList.sort()
    # final sorted list
    listSorted = []
    for key in sortList:
        listSorted.append(sortDict[key])

    # find the gaps
    hightestFileNum = sortList[-1]
    gaps = False
    for i in range(hightestFileNum):
        if i not in sortList:
            if i == 0:
                continue
            print(f'{prefix}{i} is missing')
            gaps = True

    # if the user chooses to rename files
    if gaps:
        choice = pyip.inputYesNo(prompt = 'Gaps found. Rename the files?: ')
        if choice == 'yes':
            # rename the list from 1 to length of list
            counter = 1
            for item in listSorted:
                shutil.move(item, str(item.parent) + os.sep + prefix + str(counter) + item.suffix)
                counter += 1
            print("Files renamed successfully")
        else:
            print("Didn't change the filenames")
    else: 
        print("No gaps found in the filenames")

    # insert gap at a position
    if len(sys.argv) > 1:
        try:
            insertPosition = int(sys.argv[1])
        except:
            sys.exit("Wrong input")

        # insert starting from the last file to avoid filename overlapping
        fileGapInsert = False
        for i in range(len(listSorted), insertPosition - 1, -1):
            filename = Path(dirChoice) / (prefix + str(i) + Path(item).suffix)
            toName = Path(dirChoice) / (prefix + str(i + 1) + Path(item).suffix)

            if not os.path.exists(filename):
                continue
            shutil.move(filename, toName)
            fileGapInsert = True
        
        if fileGapInsert:
            print(f"Gap inserted successfully at position: {insertPosition}")
        
        

if __name__ == '__main__':
    main()

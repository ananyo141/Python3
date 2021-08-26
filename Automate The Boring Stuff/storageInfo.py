#!python3
# This program analyzes the directory input by the user for size, file number.
import tkinter.filedialog, os

def convertMB(size_bytes):
    '''(int) ---> float
    Return the given size in bytes in Megabyte.
    '''
    return round(size_bytes / (1000 * 1000), 2)

# A dict of dicts to hold information about each folder
dirInfo = {}

def main():
    print("Choose the directory you want to analyze")
    while True:
        dirChoice = tkinter.filedialog.askdirectory()
        if dirChoice:
            break

    for item in os.listdir(dirChoice):
        itemPath = os.path.join(dirChoice, item)
        if os.path.isdir(itemPath):
            subfolders = 0
            files = 0
            totalSize = 0
            for directory, subdir, filenames in os.walk(itemPath):
                subfolders += len(subdir)
                for file in filenames:
                    files += 1
                    try:
                        fileSize = os.path.getsize(os.path.join(directory, file))
                    except FileNotFoundError:
                        continue
                    totalSize += fileSize
                    # Display size over 100 MB
                    if convertMB(fileSize) > 100:
                        print(f'{file} size is more than 100 MB - {convertMB(fileSize)} MB')
                    
            dirInfo[item] = {'subfolders': subfolders, 'files': files, 'totalsize': convertMB(totalSize)}

    # Display folder properties
    for folder in dirInfo.keys():
        print(f'\n{folder} Info:-')
        print(f"Files: {dirInfo[folder]['files']}")
        print(f"Subfolders: {dirInfo[folder]['subfolders']}")
        print(f"Total Size: {dirInfo[folder]['totalsize']} MB")

    # Find the folders with maximum size and file count
    maxSize = maxSizeFolder = maxFile = maxFileFolder = None
    for folder, info in dirInfo.items():
        if maxSize == None and maxFile == None:
            maxSize = info['totalsize']
            maxFile = info['files']
            maxSizeFolder = folder
            maxFileFolder = folder
        if info['totalsize'] > maxSize:
            maxSize = info['totalsize']
            maxSizeFolder = folder
        if info['files'] > maxFile:
            maxFile = info['files']
            maxFileFolder = folder

    print(f'\n{maxSizeFolder} is occupying maximum disk space with {maxSize} MB\n{maxFileFolder} is the folder with maximum number of files: {maxFile}')


if __name__ == '__main__':
    main()
    
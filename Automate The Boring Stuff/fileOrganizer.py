#!python3
# This program copies or moves (arranges) files in a folder according to their file extensions.
import tkinter.filedialog, threading, shutil, os, sys
from pathlib import Path
from ModuleImporter import module_importer
pyip = module_importer('pyinputplus', 'pyinputplus')
send2trash = module_importer('send2trash', 'send2trash')

def inputDir():
    '''(NoneType) ---> Str
    Ask the user to enter a directory and validate user input to return the directory path.
    '''
    chosenDir = tkinter.filedialog.askdirectory()
    if chosenDir:
        return os.path.normpath(chosenDir)
    else:
        sys.exit("No directory chosen.\n")

def organizer(extension, userDir, destinationDir):
    extensionDir = os.path.join(destinationDir, extension.lstrip('.').upper())
    os.makedirs(extensionDir, exist_ok = True)
    for directory, subdir, filenames in os.walk(userDir):
        for file in Path(directory).glob('*'+extension): 
            # if the file already exists               
            if (Path(extensionDir) / file.name).exists():
                copyfileNumber = 1
                # find the latest copy index
                while True:
                    newFileName = extensionDir + os.sep + file.stem + '_copy' + \
                    str(copyfileNumber) + file.suffix
                    if not os.path.exists(newFileName):
                        break
                    copyfileNumber += 1
                
                # rename the file with the new copy number
                shutil.copy(file, newFileName)
            else:
                shutil.copy(file, extensionDir)

def main():
    print("Choose the directory to clean and organize")
    userDir = inputDir()

    # Give user to either organize files in-situ or a different directory
    choice = pyip.inputMenu(['Rearrange the files at the current directory','Use a different directory to save the structured file-system'], prompt="Choose Preference:\n", numbered=True)
    if choice == 'Rearrange the files at the current directory':
        rearrange = True
        destinationDir = userDir + '_arranged'
        os.makedirs(destinationDir, exist_ok = True)
    else:
        rearrange = False
        print("Choose the folder to save arranged files")
        destinationDir = inputDir()
    
    fileExtensions = []
    # Crawl the directory to find all the available file extensions
    for directory, subdir, filenames in os.walk(userDir):
        for filename in filenames:
            fileExtensions.append(Path(filename).suffix)
    
    # Delete duplicate extensions: Ordering is lost
    fileExtensions = list(set(fileExtensions))

    # Crawl the directory again to copy these files according to their extension in a new directory
    threads = []    # keeping threads
    for extension in fileExtensions:
        organizingThread = threading.Thread(target = organizer, 
                                            args = [extension, userDir, destinationDir])
        threads.append(organizingThread)
        organizingThread.start()
    
    # wait for all thread operations to finish
    for thread in threads:
        thread.join()
        
    if rearrange:
        deletePrevFileSystem = pyip.inputYesNo(prompt="Do you want to delete the previous folder?: ")
        if deletePrevFileSystem == 'yes':
            try:
                send2trash.send2trash(userDir)
            except Exception as err:        # in case permission is denied by os
                print("Permission Denied\n" + str(err) + '\n')
                sys.exit(f"You can find the organised files at {destinationDir}")

            os.rename(destinationDir, userDir)
            print("Previous filesystem was organized successfully")
        else:
            print(f"You can find the organised files at {destinationDir}")
    else:
        print(f"The files were organized successfully at {destinationDir}")


if __name__ == '__main__':
    main()

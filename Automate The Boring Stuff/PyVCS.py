#!python3
# This Program creates a version control system that backs up and manages the repositories in zip format

import tkinter.filedialog, zipfile, os, time, datetime
import pyinputplus as pyip
from pathlib import Path

def confirmation(prompt):
    '''(str) ---> Bool
    Returns boolean True/False according to if the user consents to a given operation.
    '''
    if pyip.inputYesNo(prompt = prompt, limit=3) == 'yes':
        return True

def clear_console():
    '''(NoneType) --> NoneType
    Clears the console. Works for windows, linux or macOS systems.
    '''
    if not os.name == 'nt':
        os.system('clear')
    else:
        os.system('cls')

def timestamp():
    '''(NoneType) ---> NoneType
    Displays the current date and time of operation
    '''
    currentTimeDetails = datetime.datetime.now()
    print("Last successful attempt at:")
    print(f'Date: {currentTimeDetails.day}/{currentTimeDetails.month}/{currentTimeDetails.year}', end=' ')
    print(f'at Time:{currentTimeDetails.hour}:{currentTimeDetails.minute}:{currentTimeDetails.second}')

# Any folder the user chooses will be backed up in the HOME directory/PyVCS
PyVCSDir = Path.home() / 'PyVCS'

def main():
    clear_console()
    print(" Welcome to the Python Version Control System (PyVCS) ".center(100, '*'))
    print("Script written by:- Ananyobrata Pal\nEnter -0 -HELP for additional information")

    # select the active directory or option to select folder via gui
    dirChoice = pyip.inputMenu(['Use the current directory for VC', 'Use different directory'],
                                prompt="Choose directory to backup\n", numbered=True)
    if dirChoice == "Use the current directory for VC":
        dirChoice = Path.cwd()
    elif dirChoice == 'Use different directory':
        dirChoice = tkinter.filedialog.askdirectory()
        while not dirChoice:
            print("Please enter the operating directory for PyVCS")
            dirChoice = tkinter.filedialog.askdirectory()

    print(f'Current directory set as {dirChoice}')

    while True:
        if not PyVCSDir.exists():
            os.makedirs(PyVCSDir)
    
        choice = pyip.inputRegex(r'^(-\w+((\s-+\w+)+))+(.*)?$', prompt=">>>: ")
        choice = choice.split()
        
        # Save the user entered repository name for reference
        repoName = PyVCSDir / (choice[0].lstrip('-') + '_pyvcs.zip')

        # COMMANDS: -repo -COMMIT and -repo -CREATE
        if choice[1].lower() == '-commit' or choice[1].lower() == '-create':
            commit = False
            # Commits user directory to existing repo: -COMMIT
            if choice[1].lower() == '-commit':
                commit = True
                if not repoName.exists():
                    print("Repository does not exist. Create using -repo -CREATE")
                    continue
            else:
                if repoName.exists():
                    print("Repository already exists. Commit using -repo -COMMIT ")
                    continue

            # creates a new repository: -CREATE (or, continues for -COMMIT)
            repo = zipfile.ZipFile(repoName, 'w')
            for directory, subdirectory, filenames in os.walk(dirChoice):
                # Write the directory
                directory = os.path.relpath(directory, start = dirChoice)
                repo.write(directory, compress_type = zipfile.ZIP_DEFLATED)
                print(f"Adding files in {directory}...")
                # Write all the files in the directory
                for filename in filenames: 
                    print(f"Adding file {directory}{os.sep}{filename}...")
                    repo.write(os.path.join(directory, filename), compress_type = zipfile.ZIP_DEFLATED)
                    time.sleep(0.15)

            repo.close()
            if commit:
                print("Repository Version successfully updated")
            else:
                print("Repository successfully created")
            timestamp()

        # COMMAND: -repo -ADD <filename> 
        # Adds a single file to the repository
        elif choice[1].lower() == '-add':
            try:
                fileToAdd = choice[2]
            except IndexError:
                print("No filename given. Operation Unsuccessful")
                continue

            repo = zipfile.ZipFile(repoName, 'a')
            repo.write(fileToAdd)
            repo.close()
            print(f"File:{fileToAdd} successfully added to repository:{os.path.basename(repoName)}")
            timestamp()

        # COMMAND: -repo -PULL
        # extracts the repository into the current directory
        elif choice[1].lower() == '-pull':
            print("Initiating Pull Request")
            repo = zipfile.ZipFile(repoName, 'r')
            repo.extractall(dirChoice)
            repo.close()
            print("Repository cloned successfully")
            timestamp()

        # COMMAND: -0 -STATUS
        # shows the backed up folders, file size and compression size details
        elif choice[1].lower() == '-status':
            if len(list(PyVCSDir.glob('*_pyvcs.zip'))) == 0:
                print("No repositories found. Use -repo -CREATE to create a repository")
                continue
            for repository in PyVCSDir.glob('*_pyvcs.zip'):
                print(f'Repository Available: {repository}')
                repo = zipfile.ZipFile(repository, 'r')
                for files in repo.namelist():
                    fileDetails = repo.getinfo(files)
                    print(f'Files found = {files}: File Size = {fileDetails.file_size} bytes, Compressed Size: {fileDetails.compress_size} bytes')
                    if fileDetails.file_size > 0 and fileDetails.compress_size > 0:
                        print(f'Compression Efficiency: {round(fileDetails.file_size / fileDetails.compress_size, 2)}x size compression')
                    
                    time.sleep(0.4)
            
        # COMMAND: -0 -HELP
        # shows what can be done with this portable VCS
        elif choice[1].lower() == '-help':
            print("Welcome to Python Version Control System\nCommands:")
            helpMessage = ["-repo -CREATE: creates a new repository", "-repo -COMMIT: Commits user directory to existing repo",
                           "-repo -ADD <filename>: Adds a single file to the repository",
                           "-repo -PULL: extracts the repository into the current directory", "-repo -DELETE: deletes the repo(zip archive) selected",
                           "-0 -DELETE --all: deletes all the repo in the HOME directory", "-0 -STATUS: shows the repositories, their file size and compression size details",
                           "-0 -HELP: shows what can be done with this portable VCS", "-0 -EXIT: Exit the program"]
            for messages in helpMessage:
                print(('* ' + messages).rjust(len(messages)+7))

        # COMMAND: -repo -DELETE
        # deletes a repo selected
        elif len(choice) <= 2 and choice[1].lower() == '-delete':
            if confirmation(f'Are you sure you want to delete {os.path.basename(repoName)}? This operation is irreversible: '):
                os.unlink(PyVCSDir / repoName)
                print(f'{os.path.basename(repoName)} successfully deleted')
                timestamp()
            else:
                print("Cancelled")

        # COMMAND: -0 -DELETE --all
        # deletes all the repo in the HOME directory
        elif len(choice) > 2 and choice[1].lower() == '-delete':
            if choice[1].lower() + choice[2].lower() == '-delete--all':
                if confirmation(f'Do you permanently want to delete the entire database containing all the repositories?: '):
                    for repos in PyVCSDir.glob('*_pyvcs.zip'):
                        print(f'Deleting repository {os.path.basename(repos)}...')
                        os.unlink(PyVCSDir / repos)
                    print("Repositories cleaned successfully")
                    timestamp()
                else:
                    print("Cancelled")

        # COMMAND: -0 -EXIT
        # exits the current session
        elif choice[1].lower() == '-exit':
            break

        else:
            print("Invalid Request. Use -0 -HELP for help")

        time.sleep(0.5)

    clear_console()
    print("Thank you for using the PyVCS")

if __name__ == '__main__':
    main()
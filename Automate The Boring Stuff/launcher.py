#! python3
# This script acts as a launcher base for all the scipts in the directory.
import tkinter.filedialog, subprocess, sys, os

# Asserts that all scripts are at the same current working directory as the launcher script

def main():
    pythonBin = tkinter.filedialog.askopenfilename(title = 'Choose the Python executable',
                                                   filetypes=[('Executable', '*')])
    if not pythonBin:
        sys.exit("Python executable not selected.")

    print("Enter the script name you want to run, 'exit' to quit.")
    while True:
        scriptName = input("> ")
        if not scriptName:
            continue
        if scriptName.lower() == 'exit':
            break

        if not os.path.exists(scriptName):
            print(f"Couldn't find {scriptName}")
            continue

        # launch the python script and wait for execution
        try:
            returnCode = subprocess.Popen([pythonBin, scriptName]).wait()
        except OSError:
            sys.exit('Invalid executable selected')

        if returnCode:
            print(f'Process terminated with error code: {returnCode}')
        else: 
            print(f'\n\nScript completed successfully with no errors (Exit code: {returnCode})')


if __name__ == '__main__':
    main() 

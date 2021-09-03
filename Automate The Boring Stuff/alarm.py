# Create an alarm that rings a user defined music at the end of time period.

import tkinter.filedialog, time, subprocess, sys, platform

def crossPlatFileOpener(filepath: str) -> int:
    ''' Open a file using the default program assigned by os and return the exit code '''

    platName = platform.system()

    if platName == 'Linux':        # for linux systems
        returnCode = subprocess.Popen(['xdg-open', filepath]).wait()  # for manjaro, start application may change
                                                                    # according to distribution
    elif platName == 'Darwin':     # for mac systems
        returnCode = subprocess.Popen(['open', filepath]).wait()
    elif platName == 'Windows':    # for windows systems
        returnCode = subprocess.Popen(['start', filepath], shell = True).wait()
    else:
        raise Exception("OS not supported")

    return returnCode       # use with caution, bhaviour depends on the operating system

def main():
    alarmFile = tkinter.filedialog.askopenfilename(title = 'Enter the file to open after countdown')
    if not alarmFile:
        sys.exit("No alarm file entered")

    try:
        waitTime = int(input("Enter seconds to wait: "))
    except ValueError:
        sys.exit("Integer excepted")
    
    print("Waiting: ")
    while waitTime > 0:
        print(waitTime, end = ' ', flush = True)    # without flush, python won't write to stdout
        time.sleep(1)
        waitTime -= 1
    print()

    # open the file
    crossPlatFileOpener(alarmFile)


if __name__ == '__main__':
    main()

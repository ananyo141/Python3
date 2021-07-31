# This program downloads the romeo juliet file from the automate site
import requests, webbrowser, pyinputplus as pyip
import tkinter.filedialog

choice = pyip.inputChoice(choices = ['visit','download'], prompt = "Do you want to open the website for Romeo Juliet or download?(Visit/Download): ")
if choice.lower() == 'visit':
    webbrowser.open('https://www.automatetheboringstuff.com/files/rj.txt')
elif choice.lower() == 'download':
    try:
        content = requests.get('https://www.automatetheboringstuff.com/files/rj.txt')
        content.raise_for_status()
    except Exception as error:
        print("Please check your internet connection and try again\n" + str(error))
        quit()
    savefile = tkinter.filedialog.asksaveasfile(defaultextension = '.txt', filetypes = [('Plain Text', '*.txt')], mode = 'wb')
    for chunk in content.iter_content(100000):
        savefile.write(chunk)
    savefile.close()
    print("The file is successfully saved in the location")
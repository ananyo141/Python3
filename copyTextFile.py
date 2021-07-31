#WAP to copy a text file entered by the user and save as a new file for the user.
#This is written and intended as an executable script:    

import tkinter.filedialog
print("Please select the file you want to copy.\n")
file=tkinter.filedialog.askopenfile()
if file:
    try:
        contents=file.read()
    except:
        print("An error occurred.\nPlease check the file.\n")
        quit()
    file.close()
    print("Please select where you want to copy to.\n")
    to_file=tkinter.filedialog.asksaveasfile()
    if to_file:
        try:
            to_file.write(contents)
        except:
            print("An error occurred.\nPlease check the file.\n")
            quit()
        to_file.close()
        print("Your file was written successfully.\n")
    else:
        print("Error.You didn't select save file.Process Terminated\n")
else:
    print("You didn't select a valid file to write from.Process Terminated\n")
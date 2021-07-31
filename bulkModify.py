#WAP to modify all the text files the user chooses.

from tkinter.filedialog import askopenfilenames

content=input("Enter what you want to overwrite to the selected files:\n")
choice=input("Select 'W' if you want to overwrite and 'A' if you want to append to the files: ")

if choice=='W' or choice=='w':
    print("Select all the files you want to overwrite:\n")
    filenames=askopenfilenames(filetypes=[('Text Files','*.txt')])
    if filenames:
        for filename in filenames:
            file=open(filename,mode='w')
            file.write(content)
            file.close()
        print("Process completed. All the files were overwritten.")
    else:
        print("You cancelled the operation.")

elif choice=='A' or choice=='a':
    print("Select all the files you want to append to:\n")
    filenames=askopenfilenames(filetypes=[('Text Files','*.txt')])
    if filenames:
        for filename in filenames:
            file=open(filename,mode='a')
            file.write('\n')
            file.write(content)
            file.close()
        print("Process completed. All the files were appended to.")
    else:
        print("You cancelled the operation.")

else:
    print("You didn't enter a valid choice.")
    quit()


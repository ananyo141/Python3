# WAP to append to a text file.
# Quite smartly used an extension specific file opener prompt that seemingly terminates the need for any contingency.

from tkinter.filedialog import askopenfile

file=askopenfile(mode='a',filetypes=[('Text Files','*.txt')])
if file:
    file.write("\n")
    file.write(input("Enter what you want to append to the file: "))
    file.close()
    print("The processed file is generated successfully.\n")
else:
    print("You didn't select a file.Process terminated. Try again.")
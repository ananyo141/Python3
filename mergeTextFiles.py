# WAP to append two text files together into a new file.
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

print("Enter first file:\n")
file1=askopenfile(mode='r',filetypes=[('Text File','*.txt')])
if file1:
    contents1=file1.read()
    file1.close()
else:
    print("You didn't enter first file.")
    quit()

print("Enter the second file:\n")
file2=askopenfile(mode='r',filetypes=[('Text File','*.txt')])
if file2:
    contents2=file2.read()
    file2.close()
else:
    print("You didn't enter second file.")
    quit()

print("Enter the new file you want to merge to:\n")
file3=asksaveasfile(filetypes=[('Text File','*.txt')], defaultextension='*.txt')
if file3:
    file3.write(contents1)
    file3.write('\n')
    file3.write(contents2)
    file3.close()
    print("Process completed with zero errors.")
else:
    print("You didn't enter the destination file.")
    quit()
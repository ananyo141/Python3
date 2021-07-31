# WAP to prompt user for a text file and print it's contents on screen.
from tkinter.filedialog import askopenfilename

fileaddr=askopenfilename()
file=open(fileaddr,'r')
# Also can use file.readline(),file.readlines() or for line in file approach.
contents=file.read()
print(contents)
file.close()

# WAP to prompt the user for a text file and overwrite it with what the user enters.
from tkinter.filedialog import askopenfilename

fileaddr=askopenfilename()
if fileaddr:
	try:
	    file=open(fileaddr,'w')
	except:
	    print("You entered an invalid file format. Please Select a .txt filetype.")
	    quit()
	file.write(input("Please enter what you want to overwrite into the file you've chosen:\n"))
	print("Operation completed successfully.")
	file.close()
else:
	print("You didn't enter a file to process. Terminated.")
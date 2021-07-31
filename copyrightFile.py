# WAP to append "This is a copy" string to first and last line of the file input by the user.
from tkinter.filedialog import askopenfilename

fileaddr=askopenfilename()
if fileaddr:
	file_read=open(fileaddr,'r')
	try:
	    contents=file_read.read()
	except:
	    print("You entered an invalid file format. Please Select a .txt filetype.")
	    quit()
	file_read.close()
	file_write=open(fileaddr,'w')
	file_write.write("This is a copy\n\n")
	file_write.write(contents)
	file_write.write("\n\nThis is a copy")
	file_write.close()
	print("The operation completed successfully.\n")
else:
	print("You didn't enter a file. Process terminated.")
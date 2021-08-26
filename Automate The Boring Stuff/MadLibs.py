# MadLibs program that reads text files for ADJECTIVE, NOUN, ADVERB or VERB in the file and 
# prompt user to fill them in, and save in a new file.
import tkinter.filedialog
from ModuleImporter import module_importer
pyip = module_importer('pyinputplus', 'pyinputplus')

# Input the madlibs words from the user
adj = pyip.inputStr(prompt="Enter the adjective: ")
noun = pyip.inputStr(prompt="Enter the noun: ")
adv = pyip.inputStr(prompt="Enter the adverb: ")
verb = pyip.inputStr(prompt="Enter the verb: ")

# Read the source file and store the contents
sourceFile = tkinter.filedialog.askopenfile(mode='r')
content = sourceFile.read()
content = content.split()           # creates a list from the string
sourceFile.close()                  # close the source file

# Find and replace the placeholders
for i in range(len(content)):
    flag = False
    if content[i].endswith('.'):
        flag = True                 # Remember if the word has periods.
    if content[i].startswith('ADJECTIVE'):
        content[i] = adj
    elif content[i].startswith('NOUN'):
        content[i] =  noun
    elif content[i].startswith('ADVERB'):
        content[i] = adv
    elif content[i].startswith('VERB'):
        content[i] = verb
    if flag:
        content[i] = content[i] + '.'

# Save the MadLibs into a new text file
saveFile = tkinter.filedialog.asksaveasfile(mode='w')

# Write the contents
for i in range(len(content)):
    saveFile.write(content[i] + ' ')

# Close the savefile.
saveFile.close()
print("Your MadLibs is saved!")

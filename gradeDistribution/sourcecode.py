from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

from functions import *
# WAP to create a script that takes a gradefile from the user(according to format) and writes a new file 
# that contains the histogram distribution with the no. of students that got the grades.

'''
0-9:    *
10-19:  **
20-29:  ******
  :
90-99:  **
100:    *
According to the grades in grades file.
'''

# Read the grades into a list.
grades_file=askopenfile(mode='r',filetypes=[('Text files','*.txt')])
grade_list=findGrades(grades_file)
grades_file.close()

# Count the grades per range.
histogram=gradesDistribution(grade_list)

# Write the histogram to new file.
hist_file=asksaveasfile(mode='w',filetypes=[('Text File','*.txt')], defaultextension='*.txt')
writeHistogram(histogram,hist_file)

print("The process completed successfully")


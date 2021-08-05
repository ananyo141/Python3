# This function reads an opened file and returns a list of grades(float).
def findGrades(grades_file):
    '''(file opened for reading)-->list of float
    Return a list of grades from the grades_file according to the format.
    '''
    # Skip over the header.
    lines=grades_file.readline()
    grades_list=[]
    while lines!='\n':
        lines=grades_file.readline()
    lines=grades_file.readline()

    while lines!='':
        # No need to .rstrip('\n') newline as float conversion removes it automatically.
        grade=float(lines[lines.rfind(' ')+1:])
        grades_list.append(grade)
        lines=grades_file.readline()
    return grades_list

# This function takes the list of grades and returns the distribution of students in that range.
def gradesDistribution(grades_list):
    '''(list of float)-->list of int
    Return a list of ints where each index indicates how many grades are in these ranges:
    0-9: 0
    10-19: 1
    20-29: 2
      :
    90-99: 9
     100 : 10
    '''
    ranges=[0]*11
    for grade in grades_list:
        which_index=int(grade//10)
        ranges[which_index]+=1

    return ranges

# This function writes the histogram of grades returned by distribution.
def writeHistogram(histogram,write_file):
    '''(list of int,file opened for writing)-->NoneType
    Write a histogram of '*'s based on the number of grades in the histogram list.
    The output format:
    0-9:    *
    10-19:  **
    20-29:  ******
      :
    90-99:  **
    100:    * 
    '''
    write_file.write("0-9:   ")
    write_file.write('*' * histogram[0]+str(histogram[0]))
    write_file.write('\n')

    # Write the 2-digit ranges.
    for i in range(1,10):
        low = i*10
        high = low+9
        write_file.write(str(low)+'-'+str(high)+': ')
        write_file.write('*'*histogram[i]+str(histogram[i]))
        write_file.write('\n')

    write_file.write("100:   ")
    write_file.write('*' * histogram[-1]+str(histogram[-1]))
    write_file.write('\n')

    write_file.close

    # Self-derived algorithm, have bugs.(Not deleting for further analysis and possible debugging.)
    # for i in range(0,100,9):
    #     write_file.write(str(i))
    #     write_file.write('-')
    #     write_file.write(str(i+9))
    #     write_file.write(':')
    #     write_file.write('*'*histogram[(i//10)])
    #     write_file.write(str(histogram[(i//10)]))
    #     write_file.write('\n')
    # write_file.close()

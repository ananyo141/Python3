# WAP to return a list of averages of values in each of inner list of grades.
# Subproblem: Find the average of a list of values

def calListAvg(grades):
    '''(list of list of num)--list of num
    Return the list of average of numbers from the list of lists of numbers in grades.
    >>> calListAvg([[5,2,4,3],[4,6,7,8],[4,3,5,3,4,4],[4,35,3,45],[56,34,3,2,4],[5,3,56,6,7,6]])
    [3.5, 6.25, 3.833, 21.75, 19.8, 13.833]
    '''
    avg_list=[]
    for sublist in grades:
        total=0
        for grade in sublist:
            total+=grade
        avg_list.append(total/len(sublist))
    return avg_list
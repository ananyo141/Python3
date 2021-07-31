#WAP to calculate average of grades in nested loop format.

def calAvgGradeList(asn_grades):
    '''(list of list of [str,num])-->num
    Return the avg of grades in the list of list of str and num, num at index 1 in asn_grades.
    Precondition:The lists within the list asn_grades should be of the format ['Name',grade]
    >>>calAvgGradeList([['A',85],['B',53],['C',89]])
    75.66666666666667
    '''
    total=0
    for item in asn_grades:
        total+=item[1]
    return total/len(asn_grades)
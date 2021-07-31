#WAP to calculate the average of grades in two list format.

def calAvgTwoGradeList(list1,list2):
    '''(list of [string,num],list of [string,num])-->num
    Return the average of grades in list1 and list2 at index position 1.
    Precondition: Format should be, listName=['Name',Grade]
    >>>calAvgTwoGradeList(['Adam',68],['Eve',65])
    66.5
    '''
    return (list1[1]+list2[1])/2


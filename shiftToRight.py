#WAP to modify a list and shift each element to the right.
def shiftToRight(list):
    '''(list)-->NoneType
    Modify the list to shift each element to it's right. Last element becomes first element.
    '''
    reserved=list[-1]
    for i in range(len(list)-1,-1,-1):
        list[i]=list[i-1]
    list[0]=reserved

    # reserved=list[-1]
    # for i in range(len(list)-2,-2,-1):
    #     list[i+1]=list[i]
    # list[0]=reserved
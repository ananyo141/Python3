#WAP to modify a list, shift each elements to its left. Make sure to take first element into account(Push to last item)

def shiftToLeft(list):

    '''(list)-->NoneType
    Modify the list to shift each element to it's left, shift first item to last position.
    Precondition: len(list)>=1
    '''
    reserved=list[0]
    for i in range(1,len(list)):
        list[i-1]=list[i]
    list[-1]=reserved

    # reserved=list[0]
    # for i in range(len(list-1)):
    #     list[i]=list[i+1]
    # list[-1]=reserved

#WAP to define a function that takes two lists of num and adds the corresponding items to return a new list.

def addList(list1,list2):
    '''(list of num,list of num)-->list of num
    Add two lists list1 and list2 about their corresponding positions and return a new list.
    Precondition:len(list1)<=len(list2)
    >>>addList([1,2,3],[2,3,4])
    [3,5,7]
    '''
    new_list=[]
    for i in range(len(list1)):
        new_list.append(list1[i]+list2[i])
    return new_list
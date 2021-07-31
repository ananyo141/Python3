#WAP to modify the given list and double alternative objects in a list
def doubleAltObj(list):
    '''(list)--> NoneType
    Modify the list so that every alternative objet value is doubled, starting at index 0.
    '''
#   for i in range(0,len(list),2):
#       list[i]*=2
    i=0
    while i<len(list):
        list[i]*=2
        i+=2

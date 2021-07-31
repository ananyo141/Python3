def perim(s1,s2,s3):
    '''(num,num)--> num
Return the perimeter of a triangle of sides s1,s2 and s3.
>>>perim(3,2,4)
9
>>>perim(9,6,7)
22
'''
    return s1+s2+s3

def semiperim(s1,s2,s3):
    '''(num,num)--> float
Return the semiperimeter of the given triangle of sides s1,s2 and s3
>>>semiperim(3,4,6)
6.5
>>>semiperim(9,4,3)
8.0
'''
    perimeter=perim(s1,s2,s3)
    return perimeter/2

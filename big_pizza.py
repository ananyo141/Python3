from area_of_triangle import area

def getBigger(b1,h1,b2,h2):
    '''(num,num)-->num
Return the bigger of two slices of triangular pizza of given base and heights.
>>>getBigger(4,5,2,3)
'''
    if area(b1,h1)>area(b2,h2):
        print("Take the first slice")
        return area(b1,h1)
    elif area(b1,h1)<area(b2,h2):
        print("Take the second slice")
        return area(b2,h2)
    elif area(b1,h1)==area(b2,h2):
        print("Whichever has more toppings!")
    else:
        print("While you were writing a program, the fat boy ate both pizza")
        

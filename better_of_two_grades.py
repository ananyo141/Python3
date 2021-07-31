#WAP to find the better of two grades

def findBetter(grade1,grade2):
    '''(num,num)--> num
	Return the better of two grades
	>>>findBetter(96,92)
	A got better grades, 96
	96
	>>>findBetter(85,100)
	B got better grades, 100
	100
	'''
    if grade1>grade2:
        print("A got better grades,", grade1)
        return grade1
    elif grade2>grade1:
        print("B got better grades,",grade2)
        return grade2
    else:
        print("Both got same, probably cheated off the other XD")

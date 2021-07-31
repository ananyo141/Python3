#WAP to print any given no(less than 100) to 100
def uptoHundred(num):
    '''(num)-->NoneType
    Print from the given number upto 100. The given num should be less than equal to 100.
    >>>uptoHundred(99)
    >>>uptoHundred(1)
    '''
    while(num<=100):
        print(num)
        num+=1
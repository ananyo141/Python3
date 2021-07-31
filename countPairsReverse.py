#WAP to count the number of same neighbouring pais in a string in reverse.
def countPairsReverse(string):
    '''(str)-->int
    Return the number of same neighbouring pairs of characters in given string starting from last, in reverse order.
    >>> countPairsReverse("existential")
    0
    >>> countPairsReverse("errogennous")
    2
    '''
    pairs=0
    for i in range(len(string)-1,0,-1):
        if string[i]==string[i-1]:
            pairs+=1
    return pairs

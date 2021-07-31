#WAP to count the number of neigbouring pairs of characters that are same in a given string.
def countPairs(string):
    '''(str)-->int
    Return the number of same neighbouring pairs of characters in given string.
    >>>countPairs("abbisscoss")
    3
    >>>countPairs("Committee")
    3
    '''
    pairs=0
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            pairs+=1
    return pairs

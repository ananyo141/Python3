#WAP to compare two strings and find out the number of character matches at corresponding positions

def findStringMatch(s1,s2):
    '''(str,str)-->int
    Return the no. of matching characters at corresponding positions of strings s1 and s2.
    Precondition: len(s1)<=len(s2)
    >>>findStringMatch('abracadabra','aaranhoulta')
    4
    '''
    matches_found=0
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            matches_found+=1
    return matches_found

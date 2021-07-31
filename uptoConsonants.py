#WAP to return a string of consonants until a vowel is encountered
def uptoConsonants(str):
    '''(str)-->str
    Return a string of consonants from the given string until a vowel is encountered.
    >>>uptoConsonants("hello")
    >>>uptoConsonants("nice to see you")
    '''
    i=0
    collect=''
    while i<len(str) and (str[i] in 'aeiouAEIOU'):
        collect= collect+str[i]
        i+=1
    return collect

#WAP to keep printing until finding a vowel
def uptoVowel(str):
    '''(str)-->NoneType
    Print the given string upto vowel.
    >>>uptoVowel("Amber")
    >>>uptoVowel("Herd")
    '''
    i=0
    while i<len(str) and not (str[i] in 'aeiouAEIOU'):
        print(str[i])
        i+=1

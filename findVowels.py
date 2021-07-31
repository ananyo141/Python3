#WAP to find and return vowels from given string.
def collect_vowels(string):
    '''(str)--> str
    Return the vowels in the given string.
    '''
    curr_vowels=''
    for i in string:
        if i in 'aeiouAEIOU':
            curr_vowels=curr_vowels+','+i
    return curr_vowels
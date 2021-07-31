#WAP to count vowels in a given string
def countVowels(string):
    '''(str)--> int
    Return the no of vowels in the given string
    >>>count_vowels("Jack")
    >>>count_vowels("Fargo")
    '''
    curr_count=0
    for i in string:
        if i in 'aeiouAEIOU':
            curr_count +=1
    return curr_count
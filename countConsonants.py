#WAP to count consonants in a given string
def count_consonants(str):
    '''(str)-->int
    Return the number of consonants in a given string
    >>>count_consonants('HAPPY')
    >>>count_consonants('hello')
    '''
    curr_count=0
    for i in str:
        if i not in 'aeiouAEIOU':
            curr_count +=1
    return curr_count
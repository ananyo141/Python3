#WAP to return the consonants of the given string
def collect_consonants(str):
    '''(str)-->str
    Return the consonants in the given string
    >>>collect_consonants("Hey there")
    >>>collect_consonants("Happy now")
    '''
    curr_consonants=''
    for i in str:
        if i not in 'aeiouAEIOU':
            curr_consonants= curr_consonants+','+i
    return curr_consonants
# WAP that takes a list value as an argument and returns a string with all the items separated by 
# a comma and a space, with 'and' inserted before the last item.

def getListStr(list: list) -> str:
    '''Return a string with all the items in the list separated by a comma and a space,
    with 'and' inserted before the last item.

    >>>getListStr(['', '', 'apples', '','guava','tofu','cat', ''])
    'apples, guava, tofu and cat.'
    '''
                                    ### Note To Debugger ###
    # Removing empty strings in list gave undefined behaviour, empty strings were not stored 
    # with proper indexes, duplicate indexes were found. Maybe this is how python stores empty strings in lists.
    # That's why traditional methods aren't working, had to modify the input delivery system to prohibit
    # empty strings in the first place. 
                                ### DELETED PREVIOUS OBSOLETE CODE ###

    # build a list that is devoid of empty strings
    nonEmptyList = []
    for item in list:
        if item != '':
            nonEmptyList.append(item)
    # build a string made from the non-empty list
    nonEmptyStr = ''
    for i in range(len(nonEmptyList)):
        nonEmptyStr += str(nonEmptyList[i])
        if i < len(nonEmptyList) - 2:
            nonEmptyStr += ', '
        elif i < len(nonEmptyList) - 1:     # this is only checked if the first one fails
            nonEmptyStr += ' and '
        elif i < len(nonEmptyList):
            nonEmptyStr += '.'
    
    return nonEmptyStr

def main():
    # Default: ['apples', 'guava', 'tofu', 'cat']
    stringList = []
    while True:
        string = input("Enter the strings('done' to exit): ")
        if string.lower() == 'done':
            break
        stringList.append(string)

    print(getListStr(stringList))

if __name__ == '__main__':
    main()

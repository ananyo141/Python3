# WAP that takes a list value as an argument and returns a string with all the items separated by 
# a comma and a space, with 'and' inserted before the last item.

def getListStr(list):
    '''(list)-->str
    Return a string with all the items in the list separated by a comma and a space,
    with 'and' inserted before the last item.
    >>>getListStr(['apples','guava','tofu','cat'])
    'apples, guava, tofu, and cat'
    '''

                                    ### Note To Debugger ###
    # Removing empty strings in list gave undefined behaviour, empty strings were not stored 
    # with proper indexes, duplicate indexes were found. Maybe this is how python stores empty strings in lists.
    # That's why traditional methods aren't working, had to modify the input delivery system to prohibit
    # empty strings in the first place. 
                                    ### DELETED PREVIOUS OBSOLETE CODE ###

    listAsStr = ''
    nonEmptyItems = 0
    for item in list:
        if str(item) != '':
            nonEmptyItems += 1

    print(nonEmptyItems)
            
    for index, item in enumerate(list):
        if str(item) == '':
            continue
        listAsStr += str(item)
        if index == nonEmptyItems - 2:
            listAsStr += ' and '
        elif index != len(list) - 1:
            listAsStr += ', '
    
    return listAsStr

def main():
    # Default: ['apples', 'guava', 'tofu', 'cat']
    string=input("Enter the strings('done' to exit): ")
    stringList=[]
    while string != 'done':
        # if len(string) < 1:
        #     string=input("Enter the strings('done' to exit): ")
        #     continue

        stringList.append(string)
        string=input("Enter the strings('done' to exit): ")

    print(getListStr(stringList))

if __name__ == '__main__':
    main()

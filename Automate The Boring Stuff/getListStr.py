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

    # Delete any empty string in list
    for individualString in list:
        if len(individualString) == 0:
            del list[list.index(individualString)]      # also tried with del and getting each index in-situ

    # Exit and return None if there is no string in the list
    if len(list) <1:
        print("No string detected")
        return

    collect=''
    for i in range(len(list)-1):
        collect=collect+list[i]+','+' '
    collect=collect+'and '+list[len(list)-1]
    return collect


def main():
    # Default: ['apples', 'guava', 'tofu', 'cat']
    string=input("Enter the strings('done' to exit): ")
    stringList=[]
    while string != 'done':
        if len(string) < 1:
            string=input("Enter the strings('done' to exit): ")
            continue

        stringList.append(string)
        string=input("Enter the strings('done' to exit): ")

    print(getListStr(stringList))

if __name__ == '__main__':
    main()
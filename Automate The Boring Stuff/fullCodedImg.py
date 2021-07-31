# WAP to print the nested list to uncover the full image.


def fullCodedImg(nestedList):
    '''(list of list of single char)-->NoneType
    Print the all the elements inside of the nested list.
    '''
    for i in range(len(nestedList[0])):
        for list in nestedList:
            print(list[i],end='')
        print('\n')



grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

fullCodedImg(grid)

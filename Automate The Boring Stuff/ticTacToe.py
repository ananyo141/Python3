theBoard={'topL':' ','topM':' ','topR':' ','midL':' ','midM':' ','midR':' ','lowL':' ','lowM':' ','lowR':' '}

def printBoard():
    '''(NoneType)-->NoneType
    Print the current state of the board.
    '''
    print(theBoard['topL']+'|'+theBoard['topM']+'|'+theBoard['topR'])
    print('-+-+-')
    print(theBoard['midL']+'|'+theBoard['midM']+'|'+theBoard['midR'])
    print('-+-+-')
    print(theBoard['lowL']+'|'+theBoard['lowM']+'|'+theBoard['lowR'])

printBoard()
print("The board doesn't look good while empty. Press enter to start a new game")

if input()=='':
    print("Let the game begin:")
    turn = 'X'
    for i in range(9):
        print("Turn for",turn,"Enter the move(on which space)")
        move=input()
        if turn=='X':
            theBoard[move] = 'X'
            turn='O'
        else:
            theBoard[move]='O'
            turn='X'
        printBoard()


else:
    print("You are missing out on all the fun!")

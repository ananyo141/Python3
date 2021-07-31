import string

def generateValidBoardPositions(valid_board_positions):
    '''(list)--NoneType
    Modify the valid board list in global scope to include all the valid chessboard positions 
    starting from '1a' to '8h'.
    '''
    for num in range(1, 9):
        for alpha in range(0, 8):
            valid_board_positions.append(str(num)+string.ascii_letters[alpha])


def returnPieces(checkboard,valid_board_positions):
    '''(dict)-->dict
    Return a pieces dict from the position-pieces checkboard dict.
    '''
    allPieces = {}
    validation=True
    for position in list(checkboard):
        if position not in valid_board_positions:
            validation=False
            break
    if validation==False:
        wrongPositions=[]
        for position in list(checkboard):
            if position not in valid_board_positions:
                wrongPositions.append(position)
        print("You didn't enter correct positions for: ",wrongPositions)
        quit()
            

    for pieces in checkboard.values():
        allPieces.setdefault(pieces, 0)
        allPieces[pieces] += 1
    return allPieces
    


def isValidCheckboard(piecesDict):
    '''(dict)-->Boolean
    Return boolean T/F according to if the pieces quantity conditions are met and valid.
    '''
    if ((piecesDict.get('bking',0) == 1 and piecesDict.get('wking',0) == 1) #
    and (str(piecesDict.keys()).startswith('b') <= 16) and (str(piecesDict.keys()).startswith('w') <= 16) #
    and (piecesDict.get('bpawns', 0) <= 8 and piecesDict.get('wpawns', 0) <= 8)):
        return True
    else:
        return False

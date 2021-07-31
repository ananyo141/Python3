# WAP to check if a checkboard is valid and return a t/f boolean.
# Conditions: A valid board must have exactly:
# 1 black king and exactly one white king. Each player can only have at most 16 pieces,
# at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'. The piece name begins with
# either a 'w' or 'b' to represent white and black, followed by 'pawn', 'king', 'bishop', 'rook','queen', or
# 'king'. This function should detect when a bug has resulted in an improper chess board.

from functions import *

chessBoard = {}
chessBoardDefault = {'1h': 'bking', '6c': 'wqueen',
                     '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

valid_board_positions = []
generateValidBoardPositions(valid_board_positions)


# Give option to choose to enter checkboard or use from given source code.
prompt ="Do you want to enter your chess board or use the one from source code?\n(Type 'Enter' to input yours else 'default'):"
choice=input(prompt)

if choice.lower()=='enter':
    place=input("Enter the piece position:(done to finish) ")
    while place.lower()!='done':
        piece=input("Enter the piece: ")
        chessBoard[place]=piece
        place = input("Enter the piece position:(done to finish) ")

elif choice.lower()=='default':
    chessBoard=chessBoardDefault
else:
    print("You didn't enter a valid choice")

dictPieces=returnPieces(chessBoard,valid_board_positions)
print(isValidCheckboard(dictPieces))

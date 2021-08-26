# Conway's Game of Life
import random, time, copy, sys, os

character=input("Enter the character you want to play the game with: ")
WIDTH = 60
HEIGHT = 20

def clear():    
    '''(None) -> None
    Clear the terminal screen'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Create a list of list of cells:
nextCells=[]
# List of columns
for x in range(WIDTH):
    column = []
    # Column list of characters
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:  # giving 50-50% chance for dead or alive cells.
            column.append(character)    # living cell
        else:
            column.append(' ')
    nextCells.append(column)

while True:     # main program loop
    clear()
    currentCells=copy.deepcopy(nextCells)
    # print currentCells according to x-y table
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end='')
        print()     # print a newline

    # Calculate next step's cells based on current cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbouring cell coordinates:
            # % WIDTH (Remainder) used to ensure value remains between 0 and WIDTH-1
            # (as it controls overflow and rounds up to 0 everytime becomes equal to width)
            leftCoordinate = (x-1) % WIDTH
            rightCoordinate = (x+1) % WIDTH
            aboveCoordiate = (y-1) % HEIGHT
            belowCoordinate = (y+1) % HEIGHT

            # Count number of living neighbours:
            numNeighbours = 0
            if currentCells[leftCoordinate][aboveCoordiate] == character:
                numNeighbours +=1                                               # top left cell
            if currentCells[x][aboveCoordiate] == character:
                numNeighbours +=1                                               # top cell
            if currentCells[rightCoordinate][aboveCoordiate] == character:
                numNeighbours +=1                                               # top right cell
            if currentCells[rightCoordinate][y] == character:
                numNeighbours +=1                                               # right cell
            if currentCells[leftCoordinate][y] == character:
                numNeighbours +=1                                               # left cell
            if currentCells[leftCoordinate][belowCoordinate] == character:
                numNeighbours +=1                                               # bottom left cell
            if currentCells[x][belowCoordinate] == character:
                numNeighbours +=1                                               # bottom cell
            if currentCells[rightCoordinate][belowCoordinate] == character:
                numNeighbours +=1                                               # bottom right cell

            # Setting cells based on Conway's Game of Life rules:
            # Living cells with 2 or 3 living neighbouring cells live:
            if currentCells[x][y] == character and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = character

            # Dead cells with 3 living neighbours come alive:
            elif currentCells[x][y] == ' ' and (numNeighbours == 3):
                nextCells[x][y] = character

            # else everything dies or remains dead:
            else:
                nextCells[x][y] = ' '
    try:
        time.sleep(0.2)
    except:
        clear()
        print("\n","Thanks for playing the Conway's Game of Life".center(50,'-'))
        sys.exit()

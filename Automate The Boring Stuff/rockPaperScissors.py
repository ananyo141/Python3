# WAP to create a rock,paper,scissors game.
import random

def roundResult(playerMove,opponentMove):
    '''(str,str)-->Boolean/NoneType
    Return true or false according to if playerMove has defeated opponentMove
    according to the rules of rock,paper,scissors.
    '''

    if playerMove.lower() =='r' or playerMove.lower() == 'rock':
        if opponentMove.lower() == 'r' or opponentMove.lower() == 'rock':
            return None
        elif opponentMove.lower() == 'p' or opponentMove.lower() == 'paper':
            return False
        elif opponentMove.lower() == 's' or opponentMove.lower().startswith('scissor') :
            return True
        else:
            print("Wrong move by Opponent")
            return "invalid turn"

    elif playerMove.lower() == 'p' or playerMove.lower() == 'paper':
        if opponentMove.lower() == 'r' or opponentMove.lower() == 'rock':
            return True
        elif opponentMove.lower() == 'p' or opponentMove.lower() == 'paper':
            return None
        elif opponentMove.lower() == 's' or opponentMove.lower().startswith('scissor'):
            return False
        else:
            print("Wrong move by Opponent")
            return "invalid turn"

    elif playerMove.lower() == 's' or playerMove.lower().startswith('scissor') :
        if opponentMove.lower() == 'r' or opponentMove.lower() == 'rock':
            return False
        elif opponentMove.lower() == 'p' or opponentMove.lower() == 'paper':
            return True
        elif opponentMove.lower() == 's' or opponentMove.lower().startswith('scissor'):
            return None
        else:
            print("Wrong move by Opponent")
            return "invalid turn"

    else:
        print("Wrong move by Player")
        return "invalid turn"


def main():
    moves = ["rock","paper","scissors"]
    print("ROCK, PAPER, SCISSORS".center(len("ROCK, PAPER, SCISSORS") + 10, '*'))
    wins = ties = losses = 0
    print(f"{wins} wins, {losses} losses, {ties} ties.")

    move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ")
    while move.lower() != "q" and move.lower() != "quit" :
        aiMove = random.choice(moves)
        print(f"{move.upper()} versus...\n{aiMove.upper()}")

        result = roundResult(move,aiMove)
        if result == True:
            print("You Win!")
            wins += 1
        elif result == False:
            print("You Lost. Don't give up just yet!")
            losses += 1
        elif result == None:
            print("It is a tie!") 
            ties += 1
        else:
            print(result)

        print(f"{wins} wins, {losses} losses, {ties} ties.")
        move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ")
    else:
        print("Thanks for playing with us! Hope you liked it <3")


if __name__ == '__main__':
    main()

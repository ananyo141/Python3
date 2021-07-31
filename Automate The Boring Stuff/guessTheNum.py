# WAP to create a guessing game where the user inputs the secret number and guessing limit for his friend to play.
from random import randint

start=input("Press enter to start the game, 'quit' to exit: ")
if start=='':
    try:
        ans = int(input("Enter the number you want someone to guess: "))
        no_of_guess =int(input("Enter the number of guess you want to allot the player:"))
    except:
        print("Input is invalid")
    
    
    
    #include guessing limit
    for guessesTaken in range(1,no_of_guess+1):

        # random is to include random range
        highRange = randint((ans+10), (ans+15))
        lowRange = randint((ans-15), (ans-10))
        print("I am thinking of a number between",lowRange,"and",highRange)
        guess = input("Take a guess('quit' to exit): ")
        if guess == "quit":
            print("You quit the game.Go running back to mama!")
            quit()
        try:
            guessval=int(guess)
        except:
            print("Please enter a valid guess")
            continue
        
        if guessval==ans:
            print("Horray! You guessed correctly in",guessesTaken, "guesses!", "You beat the game")
            quit()
        elif (highRange>=guessval>ans):
            print("Your guess is too high")
            print("No. of guesses left:",(no_of_guess-guessesTaken))
        elif (lowRange<=guessval<ans):
            print("Your guess is too low")
            print("No. of guesses left:", (no_of_guess-guessesTaken))
            

        else:
            print("You went out of the guessing domain. LOL!")
            print("No. of guesses left:", (no_of_guess-guessesTaken))
    
    print("You lose HAHA!\nYou just had to guess",ans,"in",no_of_guess,"guesses you loser!")


elif start=='quit':
    print("You terminated the game! You sissy XD")
else:
    print("You entered invalid choice")
    


# WAP to ask the user how many coin tosses to make, and find out how what streak to calculate
# and the percentage of the streaks in the given tosses.

import random

def generate_coin_tosses(list,tossNum):
    '''(list)-->NoneType
    Modify the given list to generate the heads-tales coin flip results for tossNum no of tosses.
    '''
    for i in range(tossNum):
        toss=random.choice(['H','T'])
        list.append(toss)

# This approach is faulty, algorithm is updated to fit the result.  
def isListSame(list):
    '''(list)--Bool
    Return boolean true or false based on if the given list contains all same elements.
    '''
    for i in range(len(list)-1):
        if list[i] != list[i+1]:
            return False
        else:
            return True

def findStreaks(list,streakNum):
    '''(list,int)--->int
    Return the number of consecutive streakNum-number of streaks of heads or tails from the given list.
    '''
    counter = 1
    streaks = 0
    currentItem = list[0]
    for i in range(1, len(list)):
        nextItem = list[i]
        if currentItem != nextItem:
            counter = 1
            currentItem = nextItem
            continue
        elif currentItem == nextItem:
            counter += 1
        if counter == streakNum:
            streaks += 1
            counter = 0

    return streaks


def main():
    no_of_tosses = input("Enter how many times you want to toss the coin: ")
    streaksNum= input("Enter the streak number: ")
    while not (no_of_tosses.isdecimal() and streaksNum.isdecimal()):
        print("Enter integer values")
        no_of_tosses = input("Enter how many times you want to toss the coin: ")
        streaksNum = input("Enter the streak number: ")

    no_of_tosses = int (no_of_tosses)
    streaksNum = int (streaksNum)
    tossResults=[]
    generate_coin_tosses(tossResults,no_of_tosses)
    

    streaksCount=findStreaks(tossResults,streaksNum)
    print(tossResults)
    print(f"The given streaks is {streaksCount}\nStreak percentage: {((streaksCount/no_of_tosses)*100):.2f}%")


if __name__ == '__main__':
    main()

    

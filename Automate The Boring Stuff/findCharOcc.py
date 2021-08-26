# WAP to find the occurence of a character in given string. Use dictionary format.

from pprint import pprint

def findCharOcc(string):
    '''(str)-->dict
    Return the character count in the given string in a dict format.
    '''
    distribution={}
    for character in string:
        distribution.setdefault(character,0)
        distribution[character]=distribution[character]+1
    return distribution

askStr=input("Enter the string you want to evaluate the distribution: ")
charDist=findCharOcc(askStr)
pprint(charDist)

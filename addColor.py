#WAP to input colors from user and add it to list
def addColor():
    '''(NoneType)-->list
    Return the list of colors input by the user.
    '''
    colors=[]
    prompt="Enter the color you want to add, press return to exit.\n"
    color=input(prompt)
    while color!='':
        colors.append(color)
        color=input(prompt)
    return colors
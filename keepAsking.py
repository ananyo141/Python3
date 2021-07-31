#WAP to nag the user yes/no and return if say yes, keep asking if no or anything else.
def keepAsking(prompt):
    '''(str)--->str
    Prompt the user given input and keep prompting until user says yes and return it.
    '''
    ask=input(prompt)
    while ask !='Yes':
        ask=input(prompt)
    return prompt
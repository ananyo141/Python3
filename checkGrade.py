#WAP to find out if the student has passed.
def checkGrade(th_g,pr_g):
    '''(num,num)--> NoneType
    Check if the student has passed if both theory_g, and prac_g are over passing marks.
    '''
    pass_th=80
    pass_pr=50
    if th_g>=80 and pr_g>=50:
        print("You've passed! Yay!\n")
    else:
        print("You've failed. Be ready for some spanking at home!\n")

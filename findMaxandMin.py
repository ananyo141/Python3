prompt="Enter an integer number.\n"
list1=[]
ask=input(prompt)
while ask!='done':
    try:
        list1.append(int(ask))
        ask=input(prompt)
    except:
        print("Invalid input\n")
        ask=input(prompt)
if len(list1)==0:
    print("You didn't enter any number.\n")
    quit()
small=list1[0]
large=list1[0]
for i in range(len(list1)):
    if list1[i]<small:
        small=list1[i]
for i in range(len(list1)):
    if list1[i]>large:
        large=list1[i]
print("Maximum is",large,"\nMinimum is",small)

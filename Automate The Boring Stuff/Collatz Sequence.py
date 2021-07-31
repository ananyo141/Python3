# WAP to write a Collatz Sequence.
def collatz(number):
    '''(int)-->int
    Print and return int division of number by 2 if number is even or else return 3*number+1 if number is odd.
    >>>3
    10
    '''
    if (number%2)==0:
        print(number//2)
        return number//2
    elif (number%2) != 0:
        print(3*number+1)
        return 3*number+1

try:
	inNum=int(input("Enter the number you want to find the Collatz Sequence of: "))
except:
	print("You entered invalid number.")
	quit()
outNum=collatz(inNum)
while outNum!=1:
    outNum=collatz(outNum)

score = input("Enter Score: ")
try:
    score1=float(score)
except:
    print("Please enter a logical score within range.\n")
    quit()
if score1>=0.9:
    print("A\n")
elif score1>=0.8:
    print("B\n")
elif score1>=0.7:
    print("C\n")
elif score1>=0.6:
    print("D\n")
else:
    print("F\n")

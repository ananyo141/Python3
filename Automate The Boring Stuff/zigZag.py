# Create a small zigzag animation program.

import time, sys, os

os.system("clear")

indent=0
character = input("What string do you want to animate?: ")
try:
    width = int(input("How broad you want the animation to go?: "))
except:
    sys.exit("Wrong width value, process terminated SMARTASS!")

start=input("Start Animation(Y/N)?: ")
if start.lower()=='y' or start.lower().startswith('ye'):
    startAnnouncement = "Commencing animation. Use Ctrl+C to stop."
    print((startAnnouncement.center(len(startAnnouncement)+20, '-')).rjust(len((startAnnouncement.center(len(startAnnouncement)+20, '-')))+20))
    time.sleep(2)
    indentRight=True
    try:
        while True:      # using a deliberate infinite loop
            print((' '*indent).rjust(len(' '*indent)+20), end='')
            print((character*8).rjust(len(character*8)+20))
            time.sleep(0.1)   # without this, the animation would go crazy
            if indentRight:
                indent+=1
                if indent==width:
                    indentRight=False
            else:
                indent-=1
                if indent==0:
                    indentRight=True
    except KeyboardInterrupt:
        os.system("clear")
        sys.exit("\nDid you like the animation? Hope you did.\nTry out other combinations of characters and have fun!")
else:
    print("Maybe next time then.")

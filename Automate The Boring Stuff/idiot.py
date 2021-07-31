# Write a program that keeps an idiot busy for hours.
import pyinputplus as pyip
import random, time

prompt = ["Do you want to know how to keep an idiot busy for hours?\n",
          "Do you really wanna know how to keep an idiot busy for hours?\n",
          "There would be a hefty price to pay if you do, still do you want to know how to keep an idiot busy for hours?\n",
          "Want to know how to keep an idiot busy for hours?\n",
          "What price do you want to pay if you want to know how to keep an idiot busy for hours?\n",
          "Are you ready to know how to keep an idiot busy for hours?\n",
          "Warming you up to know how to keep an idiot busy for hours...\n"]

while True:
    idiotResponse = pyip.inputYesNo(random.choice(prompt))
    time.sleep(0.25)
    if idiotResponse == 'no':
        break

print("Okay, your loss! Have a nice day.")

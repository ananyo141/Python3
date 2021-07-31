# Make a mental math game.
import pyinputplus as pyip
import random, time, os

operations = ['+','-','/','*']
numberOfQuestions = 10
correctAns = 0

print("Welcome to the BrainTrainer!\nGame will be starting soon\n\
Hint: Enter just whole number for divisions, no need to enter the fraction part.")
for countdown in range(5,-1,-1):
    print(str(countdown) + '...')
    time.sleep(1)

print("Get Ready!")
time.sleep(1)
os.system('clear')

for question in range(1, numberOfQuestions+1):
    operator = random.choice(operations)
    
    if operator == '+' or operator == '-':
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, 1000)
        prompt = '#%s: %s %s %s = ' % (question,num1,operator,num2)
        if operator == '+':
            answer = num1 + num2
        else:
            answer = num1 - num2

    else:
        num1 = random.randint(-12, +12)
        num2 = random.randint(-12, +12)
        prompt = '#%s: %s %s %s = ' % (question, num1, operator, num2)
        if operator == '*':
            answer = num1 * num2

        else:
            answer = int(num1 / num2)

    try:
        # Right answers are handled by allowRegex
        # Wrong answers are handled by blockRegex
        pyip.inputStr(prompt,allowRegexes=['^%s$' % (answer)],
            blockRegexes=[('.*','Incorrect')],
            timeout=12, limit=3)

    except pyip.TimeoutException:
        print('Out of time')
        print('Correct answer was: %s' % (answer))

    except pyip.RetryLimitException:
        print('Out of tries!')
        print('Correct answer was: %s' % (answer))

    else:
        # This block runs if no exceptions were raised
        print('Correct!')
        correctAns += 1

    time.sleep(1.3) # Brief pause to let user see the result
    os.system('clear')


print('Score: %s / %s' % (correctAns, numberOfQuestions))

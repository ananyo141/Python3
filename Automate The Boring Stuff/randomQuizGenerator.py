#! python3
# Creates quizzes with questions and answers in random order, along with the answer key
import random, tkinter.filedialog
from pathlib import Path
from ModuleImporter import module_importer
pyip = module_importer('pyinputplus', 'pyinputplus')

# Quiz Data
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

quizFileNum = pyip.inputInt("How many quiz forms do you want to prepare?: ")
print("Enter the folder you want to save the files")
fileDirectory = tkinter.filedialog.askdirectory()

# Generating quiz files
for quizNum in range(quizFileNum):

    # Create the quiz and answer key files
    quizFile = open((Path(fileDirectory) / ('CapitalQuizPaper' + str(quizNum + 1) + '.txt')), 'w')
    answerKeyFile = open((Path(fileDirectory) / ('CapitalQuizAnswers' + str(quizNum + 1) + '.txt')), 'w')

    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all the 50 states, making question for each
    for questionNum in range(len(states)):

        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]

        wrongAnswers = list(capitals.values())
        wrongAnswers.remove(correctAnswer)              # remove right answer from wrong answers list

        wrongAnswers = random.sample(wrongAnswers, 3)   # take random 3 options from the wrong ans list
        answerOptions = wrongAnswers + [correctAnswer]  # prepare the answer options
        random.shuffle(answerOptions)                   # final shuffling options

        # Write the question and answer options to quiz file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')

        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')

        # Write answer key to file
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}) {correctAnswer}\n")
    
    quizFile.close()
    answerKeyFile.close()

print("The question-paper set along with setwise answer keys is created in the desired directory.")

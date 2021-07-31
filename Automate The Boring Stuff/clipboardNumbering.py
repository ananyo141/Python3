#!python3 
# WAP that takes the text in the clipboard and adds a '*' and space before each line and copies to the 
# clipboard for further usage.

import sys,pyperclip

def textNumbering(text, mode):
    '''(str,str)-->str
    Returns a ordered or unordered string according to newlines of the given text argument and 
    mode.
    '''
    textList = text.split('\n')
    if mode.lower()=='unordered':
        for i in range(len(textList)):
            textList[i] = "* "+textList[i]
    elif mode.lower()=='ordered':
        numbering = 1
        for i in range(len(textList)):
            textList[i] = str(numbering)+') '+textList[i]
            numbering += 1
    else:
        sys.exit("Invalid Choice")

    processedText = ('\n').join(textList)
    return processedText

def main():
    # Uses terminal argument as mode-choice for easier operation #
    if len(sys.argv)<2:
        sys.exit("Usage: python [filename.py] [mode]")

    choice=sys.argv[1]
    clipboard=pyperclip.paste()
    numberedText=textNumbering(clipboard,choice)
    pyperclip.copy(numberedText)
    print("Successfully completed.")

if __name__ == '__main__':
    main()


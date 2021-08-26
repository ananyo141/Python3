# Regex equivalent of the strip() function.
import re

def regexStrip(text,*toStrip):
    '''(str[,str])--->str
    Return a stripped version of the text. Strip whitespaces from both ends if toStrip isn't passed.
    '''
    if toStrip == ():       # if optional parameter is not given
        spaceRe = re.compile(r'^\s*(.*)\s*$', re.DOTALL)

        return spaceRe.sub(r'\1',text)

    if toStrip:             # if optional parameter is given
        stripVal = toStrip[0]       # optional argument returns a tuple of the value passed
        stripRe = re.compile(fr'''(
            ^{stripVal}*
            (.*)
            {stripVal}*$
        )''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
        
        return stripRe.sub(r'\2',text)

def main():
    print("This program uses the regex equivalent of the strip() function")
    text = input("Enter the text you want to strip:\n")
    optionalArgument = input("Enter what you want to strip (return to opt for no optional parameter): ")

    if optionalArgument == '':
        strippedText = regexStrip(text)
    if len(optionalArgument) > 0:
        strippedText = regexStrip(text, optionalArgument)
    print("The stripped text is:",strippedText)

if __name__ == '__main__':
    main()
    
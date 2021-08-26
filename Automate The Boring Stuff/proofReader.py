#!python3
# Check the copied text for common typos such as multiple spaces, accidentally repeated words or multiple 
# exclamation, commas or dots (at the end of sentences).
import re
from ModuleImporter import module_importer
pyperclip = module_importer('pyperclip', 'pyperclip')

def proofReader(text):
    '''(str)--->str
    Return a modified string where the multiple spaces, accidentally repeated words or multiple 
    exclamation, commas and/or dots (at the end of sentences) are corrected.
    '''
    typoRegex = re.compile(r'''(
        ((\s)\s+)?                     # Multiple Spacing
        # A heavily modified version of Stack Overflow Code Snippet (DUPLICATE WORD) #
        (\b(\w+)(?:\s+\5\b)+)?         # Repeated words       # Important: {?:} works as to forget the group enclosed. That's why when asked for appropriate groups(group 12), there was reference error.  
        ((!)\s*!+)?                    # Multiple Exclamation
        ((,)\s*,+)?                    # Multiple commas
        ((\.)\s*\.+$)?                 # Multiple dots only at the end
        )''', re.VERBOSE | re.I)
    cleanedText = typoRegex.sub(r'\3\5\7\9\11', text)       # The groups are specially crafted to include only one of the matched regexes
    
    return cleanedText

def main():
    clipboard = pyperclip.paste()
    newClipboard = proofReader(clipboard)
    print("Text successfully checked and proof read.")
    pyperclip.copy(newClipboard)

if __name__ == '__main__':
    main()

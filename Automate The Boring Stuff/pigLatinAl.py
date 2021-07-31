# English to Pig Latin.
message=input("Enter the English message to translate into Pig Latin: ")

VOWELS = ('a','e','i','o','u','y')

pigLatin = [] # A list of words in Pig Latin.
for word in message.split():
    # Separate non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    # Separate non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was uppercase or title.
    wasUpper = word.isupper()
    wasTitle = word.istitle()


    word = word.lower()  # Making the word ready for insertion/translation

    # Separate the consonants at the start of the word.
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set back to uppercase or lowercase:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Assemble the word:
    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))
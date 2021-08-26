# WAP to convert user input to Pig Latin.
# Rules: 
# If a word begins with a vowel the word yay is added to the end of it.
# If it begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster is 
# moved to the end of the word followed by ay.

english=input("Enter the sentence you want to convert to Pig Latin:\n")
vowels='aeiouy'
words=english.split()
pigLatin=[]
for word in words:
    if word[0].lower() in vowels:
        word = word+"yay"
        pigLatin.append(word)
    elif word[0].isalpha():
        consonantCluster=""
        i=0
        while i<len(word) and word[i].lower() not in vowels:
            consonantCluster+=word[i]
            i+=1
        word=word.lstrip(consonantCluster)
        word=word+consonantCluster+'ay'
        word=word.lower().title()
        pigLatin.append(word)
    elif word[0].isdecimal():
        word = word
        continue

pigLatinStr = ' '.join(pigLatin)
print(pigLatinStr)

import random

def createAnagram(word):
    word = word.lower()
    word = [x for x in word]
    random.shuffle(word)
    strings = ""
    for i in word:
        strings += i
    return strings
print(createAnagram("leandro"))

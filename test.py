import random
import sys
import os
import urllib.request

def help():
    print("Help: crackerDown -a [text]")
def wordInDic(word, anagram):
    for letter in word:
        if(letter.lower() not in str(anagram.lower())):
            return False
    return True

def getAnagram():
    argv = sys.argv
    return sys.argv[2]

def getDictionary(letter):
    url = 'https://raw.githubusercontent.com/Leandro-Trinidad-QECS/Oxford-Dictionary/master/'
    url3 = '_text.txt'
    data = urllib.request.urlopen(url + letter + url3)

    return [line.decode("utf-8").strip("\n") for line in data]

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if((len(sys.argv) < 3) or sys.argv[1] != "-a"):
        help()
        exit(0)

    anagram = getAnagram()
    solved = []
    for letter in alphabet:
        for word in getDictionary(letter):
            if(wordInDic(word,anagram)):
                solved.append(word)
    
    print(solved)

if(__name__=="__main__"):
    main()

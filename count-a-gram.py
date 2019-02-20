#!/usr/bin/env python3
import random
import sys
import os
import urllib.request

def help():
# Prints out the help page #
    print("count-a-gram")
    print("Help: count-a-gram -a [text]")
    print("      count-a-gram -a [text] -l [num]")
    print("      count-a-gram -a [text] -f")
    print("      count-a-gram -a [text] -c")
    print("      count-a-gram -a [text] -c -l 10")
    print("-a    The anagram")
    print("-l    How long the output is")
    print("-f    Full anagram")
    print("-c    create anagram")

def wordInDic(word, anagram): 
# Checks if the word can be created using the anagram #
    word = word.lower()
    anagram = anagram.lower()
    for letter in word:
        if(letter not in anagram):
            return False
        else:
            anagram = anagram.replace(letter,"",1)
    return True
            
def fullwordInDic(word,anagram):
    word = word.lower()
    anagram = anagram.lower()
    if(len(word) != len(anagram)):
        return False
    for letter in word:
        if(letter in anagram):
            anagram = anagram.replace(letter,"",1)
    if(len(anagram) == 0):
        return True
    return False

def createAnagram(word):
    word = word.lower()
    word = [x for x in word]
    random.shuffle(word)
    strings = ""
    for i in word:
        strings += i
    return strings

def getAnagram():
# gets the users arguments #
    argv = sys.argv
    return sys.argv[2]


def sortArray(arry): 
# Sorts the array #
    arry.sort(key = len, reverse = True)


def getDictionary(letter):
# gets the dictionary words from my gihub page #
    url = 'https://raw.githubusercontent.com/Leandro-Trinidad-QECS/Oxford-Dictionary/master/'
    url3 = '.txt'
    data = urllib.request.urlopen(url + letter + url3)

    return [line.decode("utf-8").strip("\n") for line in data]


def main():
# main program #

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
#   if((len(sys.argv) < 3) or sys.argv[1] != "-a"):
#       help()
#       exit(0)

    anagram = ''
    listAmount = 5
    fullAnagram = False
    createAnag = False
    try:

        if((len(sys.argv) < 3) or ("-a" not in sys.argv)):
            help()
            exit(0)
        for i in range(len(sys.argv)):
            if(sys.argv[i] == "-a"):
                anagram = sys.argv[i+1]
            if(sys.argv[i] == "-f"):
                fullAnagram = True
                
            if(sys.argv[i] == "-l"):
                listAmount = int(sys.argv[i+1])
            if(sys.argv[i] == "-c"):
                createAnag = True
    except Exception as e:
        print(e)
        help()
        exit(0)

    print("-"*5 + " count-a-gram " + "-"*5)
    print("Input: %s" %(anagram))
    solved = []

    if(not fullAnagram and not createAnagram):
        for letter in alphabet:
            for word in getDictionary(letter):
                if(wordInDic(word,anagram)):
                    solved.append(word)
        sortArray(solved)
    elif(fullAnagram and not createAnagram):
        for letter in alphabet:
            for word in getDictionary(letter):
                if(fullwordInDic(word,anagram)):
                    solved.append(word)
    if(createAnag):
        for _ in range(listAmount):
            solved.append(createAnagram(anagram))
    if(len(solved) < listAmount):
        listAmount = len(solved)
    for i in range(listAmount):
        print(str("%s) %s %s" % (str(i+1), solved[i], len(solved[i]))))

    print("-"*24)

if(__name__=="__main__"):
    main()

#!/usr/bin/env python3
import random
import sys
import os
import urllib.request

def help():
# Prints out the help page #
    print("Help: crackerDown -a [text]")


def wordInDic(word, anagram): #TODO: How do i do this !!!!!
# Checks if the word can be created using the anagram #
    word = word.lower()
    anagram = anagram.lower()
    for letter in word:
        if(letter not in anagram):
            return False
        else:
            anagram = anagram.replace(letter,"",1)
    return True
            

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
    print(sys.argv)
    try:
        for i in range(len(sys.argv)):
            if(sys.argv[i] == "-a"):
                anagram = sys.argv[i+1]
            if((len(sys.argv) < 3) or ("-a" not in sys.argv)):
                help()
                exit(0)
                
            if(sys.argv[i] == "-l"):
                listAmount = int(sys.argv[i+1])
    except Exception as e:
        print(e)
        help()
        exit(0)

    print("-"*5 + " countDown " + "-"*5)
    print("Input: %s" %(anagram))
    solved = []
    for letter in alphabet:
        for word in getDictionary(letter):
            if(wordInDic(word,anagram)):
                solved.append(word)
    sortArray(solved)
    if(len(solved) < listAmount):
        listAmount = len(solved)
    for i in range(listAmount):
        print(str("%s) %s %s" % (str(i+1), solved[i], len(solved[i]))))

    print("-"*21)

if(__name__=="__main__"):
    main()

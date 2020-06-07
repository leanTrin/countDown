import json
import requests
import argparse

WORDS_URL = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json'

def get_response(url):
    resp = requests.get(url)
    resp.raise_for_status
    return resp

def load_words():
    resp = get_response(WORDS_URL)
    return resp.json()

def is_anagram(word, chars):
    """ is chars and anagram of word """
    sp = list(word.lower())
    for letter in chars.lower():
        if letter in sp:
            sp.remove(letter)

    return False if sp else True

def get_anagrams(words, chars):
    for word in words:
        if is_anagram(word, chars):
            yield word

if __name__=='__main__':
    # Solve for Conundrum
    # 
    #
    english_words = load_words()
    parser = argparse.ArgumentParser(description='Solver for the Count Down letters game')
    parser.add_argument('-c', dest='conundrum', action='store_true', help='Solve for a Conundrum')
    parser.add_argument('letters')
    args = parser.parse_args()

    anagrams = get_anagrams(english_words, args.letters)
    anagrams = list(anagrams)
    anagrams = reversed(sorted(anagrams, key=len))

    if args.conundrum:
        for word in anagrams:
            if len(word) == len(args.letters):
                print(word, len(word))
    else: 
        for i, word in zip(range(10), anagrams):
            print(word, len(word))

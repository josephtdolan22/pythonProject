import random
from collections import Counter

wordBase = '''lexington congress saratoga lafayette washington hamilton amendment constitution rochambeau yorktown revolution democracy monarchy'''
wordBase = wordBase.split(' ')
word = random.choice(wordBase)

if __name__ == "__name__":
    print("Welcome to Hangman! The theme is the American Revolution.")

    for i in word:
        print('_', end = ' ')
    print()

    playing = True
    

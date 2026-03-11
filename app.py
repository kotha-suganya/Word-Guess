
import random
from collections import Counter

# Load words from file
with open("words.txt", "r") as f:
    someWords = f.read().split()

# Random word selection
word = random.choice(someWords)

print("Guess the word!")

for i in word:
    print('_', end=' ')
print()

letterGuessed = ''
chances = len(word) + 2
flag = 0

try:
    while chances != 0 and flag == 0:
        print()
        guess = input('Enter a letter to guess: ')

        if not guess.isalpha():
            print('Enter only a LETTER')
            continue
        elif len(guess) > 1:
            print('Enter only a SINGLE letter')
            continue
        elif guess in letterGuessed:
            print('You already guessed that letter')
            continue

        # Correct guess
        if guess in word:
            letterGuessed += guess * word.count(guess)
            print("Good job! Correct guess 👍")
        else:
            print("Sorry! Wrong guess ❌")

        chances -= 1
        print("Chances left:", chances)

        # Show progress
        for char in word:
            if char in letterGuessed:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()

        # Win check
        if Counter(letterGuessed) == Counter(word):
            print("\nThe word is:", word)
            print("Congratulations, You won! 🎉")
            flag = 1
            break

    # Lose condition
    if chances == 0 and flag == 0:
        print("\nYou lost! Try again..")
        print("The word was", word)

except KeyboardInterrupt:
    print("\nBye! Try again.")

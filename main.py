import random

fileHandle = open('words.txt')
words = fileHandle.read().split()

wordToGuess = list(random.choice(words))
puzzle = []

for letter in wordToGuess:
    puzzle.append('_')
print(' '.join(puzzle))

numberOfGuesses = 10

while numberOfGuesses > 0:
    if '_' in puzzle:
        userGuess = input('Enter a letter:')
        if userGuess in puzzle:
            print('You already guessed this letter. Try a different one')
            print(' '.join(puzzle))
            continue
        elif userGuess in wordToGuess:
            indices = [i for i, x in enumerate(wordToGuess) if x == userGuess]
            for index in indices:
                puzzle[index] = userGuess
            print(' '.join(puzzle))
        else:
            print('Wrong! Try again!')
            numberOfGuesses -= 1
            print(' '.join(puzzle))
    else:
        print('You win!')
        break

if numberOfGuesses == 0:
    print('You Lose!')
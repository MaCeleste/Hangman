import random

words = ['computer', 'hairspray', 'radiator']

wordToGuess = list(random.choice(words))
puzzle = []

for letter in wordToGuess:
    puzzle.append('-')
print(puzzle)

numberOfGuesses = 8

while numberOfGuesses > 0:
    if '-' in puzzle:
        userGuess = input('Enter a letter:')
        if userGuess in puzzle:
            print('You already guessed this letter. Try a different one')
            continue
        elif userGuess in wordToGuess:
            indices = [i for i, x in enumerate(wordToGuess) if x == userGuess]
            print(indices)
            for index in indices:
                puzzle[index] = userGuess
            print(puzzle)
        else:
            print('Wrong! Try again!')
            numberOfGuesses -= 1
    else:
        print('You win!')
        break

if numberOfGuesses == 0:
    print('You Lose!')
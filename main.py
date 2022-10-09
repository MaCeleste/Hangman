import random

# This file contains the words that will be loaded onto the game.
# The words are strings of lowercase letters.

source = 'words.txt'


# This function reads the source file, converts the contents into a list.
# Then it selects one random word and converts it into a list of characters.

def get_word(file):
    filehandle = open(file)
    words = filehandle.read().split()
    return list(random.choice(words))


# Starts up a game of Hangman.

def game():
    # word_to_guess will run the get_word() function and store the word that the player has to guess

    word_to_guess = get_word(source)

    # hidden_word will store a list containing a '_' for each character in word_to_guess

    hidden_word = []
    for letter in word_to_guess:
        hidden_word.append('_')

    # Welcome message. Informs the player how many characters there are in the word to guess
    # and how many guesses they have left.
    # Displays a '_' for each unknown character.

    print('Welcome to Hangman!')
    print(f'Your word is {len(word_to_guess)} letters long.')
    print(' '.join(hidden_word))

    # number_of_guesses stores the number of tries that the player has left.

    number_of_guesses = 8

    # The following block will run while the player has guesses left. It will be interrupted if the player
    # guesses the correct word before running out of guesses.

    while number_of_guesses > 0:

        # If there are any '_' in hidden_word it means that the player has not discovered all the
        # characters yet. Therefore, they will be asked to enter a letter that will be stored
        # in the user_guess variable.

        if '_' in hidden_word:

            print(f"You have {number_of_guesses} {'guess' if number_of_guesses == 1 else 'guesses'} left")
            user_guess = input('Enter a letter:').lower()
            # This block is executed if the letter entered by the player has already been discovered.
            # If so, it asks the player to enter a different letter. Note that this case is not considered a mistake,
            # so no guesses are deducted from the remaining amount.

            if user_guess in hidden_word:
                print('You already guessed this letter. Try a different one')
                print(' '.join(hidden_word))
                continue

            # This block is executed if the player makes a correct guess. The '_' in hidden_word will
            # be replaced with the corresponding letter.

            elif user_guess in word_to_guess:
                indices = [i for i, x in enumerate(word_to_guess) if x == user_guess]
                for index in indices:
                    hidden_word[index] = user_guess
                print(' '.join(hidden_word))

            # This block is executed if the player makes an incorrect guess. One guess is deducted
            # from the remaining number_of_guesses.

            else:
                print('Wrong! Try again!')
                number_of_guesses -= 1
                print(' '.join(hidden_word))

        # If there aren't any '_' left in hidden_word it means that all the letters have been
        # discovered and the player has won.

        else:
            print('You win!')
            break

    # If the player doesn't have any guesses left, a message including the correct word is shown.

    if number_of_guesses == 0:
        print(f"You Lose! The word was {''.join(word_to_guess)}")


def main():
    # Calls the first game

    game()

    # After the first game ends, the player will be asked if they want to play again.

    while True:
        again = input('Would you like to play again? Enter Y/N:').lower()
        if again.startswith("y"):
            print("Let's play again!")
            game()
        elif again.startswith("n"):
            print("Ok. Thank you for playing!")
            break
        else:
            print('Invalid input')
            continue


# To start the game when you execute the file on the terminal

if __name__ == '__main__':
    main()

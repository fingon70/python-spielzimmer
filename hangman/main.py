import random
import os

import hangman_art
import hangman_words


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

word_to_guess = random.choice(hangman_words.word_list_red_light)

# print(f'Word to guess: {word_to_guess}')

word_length = len(word_to_guess)

display = []
for _ in range(word_length):
    display.append('_')

end_of_game = False
max_errors = len(hangman_art.stages) - 1
errors = max_errors

while not end_of_game:
    #
    print(display)
    guessed = input('Your char: ').upper()

    if guessed in word_to_guess:
        for i in range(word_length):
            if word_to_guess[i] == guessed:
                display[i] = guessed
        if '_' not in display:
            print(f"You've won. The word is '{word_to_guess}'. :=)")
            end_of_game = True
            print(hangman_art.logo)
        else:
            cls()
            print()
            if max_errors != errors:
                print(hangman_art.stages[errors])
    else:
        errors -= 1
        if errors < 0:
            end_of_game = True
            print(hangman_art.logo)
        else:
            cls()
            print(f'You lost a life!')
            print(hangman_art.stages[errors])

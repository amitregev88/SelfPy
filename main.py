from ex251 import *     # print_opening_screen
from ex10 import *      # get_secret_word
from ex841 import *     # print_hangman
from ex731 import *     # show_hidden_word     
from ex641 import *     # check_valid_input
from ex642 import *     # try_update_letter_guessed
from ex252 import *     # input_user_guess


num_of_tries = 0
MAX_TRIES = 6
old_letters_guessed = []


print_opening_screen()

secret_word = get_secret_word()

print_hangman(num_of_tries + 1)



for num_of_tries in range(MAX_TRIES):

    print("\n\n" + show_hidden_word(secret_word, old_letters_guessed))
    letter_guess = input_user_guess()
    res = try_update_letter_guessed(letter_guess, old_letters_guessed)

        




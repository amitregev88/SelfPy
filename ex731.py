def show_hidden_word(secret_word, old_letters_guessed):

    to_return = ["_"] * len(secret_word)


 
    for i, letter_in_secret_word in enumerate(secret_word):

        for letter_in_old_letters_guessed in old_letters_guessed:

            if letter_in_secret_word ==  letter_in_old_letters_guessed:

                to_return[i] = letter_in_secret_word

    return " ".join(to_return)


# def show_hidden_word (secret_word, old_letters_guessed):
#     """Displays guessed letters in the secret word, and '_' for letters that were
#     not guessed yet
#     :param: secret_word: the word to be guessed
#     :param: old_lettes_guessed: the letters that were guessted (user's input)
#     :type secret_word: list
#     :type old_lettes_guessed: list
#     :return: the updated list, with all guessed letters
#     :rtype: list
#     """
#     result = ''
#     for letter in secret_word:
#         if letter in old_letters_guessed:
#             result = result + letter + ' '
#         else:
#             result = result + "_ "
#     return result[:-1]
   

# if __name__ == "__main__":


#     print(show_hidden_word("typewriter",['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']))


from ex641 import *

def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    res = check_valid_input(letter_guessed, old_letters_guessed)

    if res:
        old_letters_guessed.append(letter_guessed)
        
        

    else:

        old_letters_guessed.sort()
    print("X\n" + " -> ".join(old_letters_guessed))

    return res


# the solve of this unit:

# NOT_UPDATED_STR = "X\n{0}"


# def check_valid_input(letter_guessed, old_letters_guessed):
#     """Checks the validation of user’s input, e.g one English letter, not entered
#     before
#     :param letter_guessed: user’s input
#     :param old_letters_guessed: previous inputs
#     :type letter_guessed: string
#     :type old_letters_guessed: list
#     :return: True if input is valid, False if not.
#     :rtype: boolean
# 	"""
#     return len(letter_guessed) == 1 and letter_guessed.isalpha() \
#            and not letter_guessed.lower() in old_letters_guessed


# def try_update_letter_guessed(letter_guessed, old_letters_guessed):
#     """Checks validation of user’s input (as in previous task).
#     if so, adds it to "old_letters_guessed" and returns True. Otherwise returns
#     False.
#     :param letter_guessed: user’s input
#     :param old_letters_guessed: previous (valid) inputs
#     :type letter_guessed: string
#     :type old_letters_guessed: list
#     :return: True if input is valid, False if not.
#     :rtype: boolean
# 	"""
#     if check_valid_input(letter_guessed, old_letters_guessed):
#         old_letters_guessed.append(letter_guessed.lower())
#         return True
#     else:
#         print_list_not_updated(old_letters_guessed)
#         return False


# def print_list_not_updated(my_list):
#     """Prints not-ypdated string.
#     :param my_list (not updates)
#     :type my_list: list
#     """
#     print(NOT_UPDATED_STR.format(" -> ".join(sorted(my_list))))












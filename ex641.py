def check_valid_input(letter_guessed, old_letters_guessed):
    '''
    Checks the validation of input (character),
    also checks if the user guessed the letters already.
    :param: letter_guessed: user guess 
    :type: string
    :old_letters_guessed: List of previous valid character guesses of the user.
    :type: list
    :return: Whether or not the input was valid
    :rtype: boolean
    '''

    letter_guessed = letter_guessed.lower()
    
    
    if len(letter_guessed) > 1:
        return False
    
    elif letter_guessed in old_letters_guessed:
        return False
    
    elif letter_guessed.isalpha():
        return True

    return False


'''
def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks the validation of userâ€™s input, e.g one English letter, not entered
    before
    :param letter_guessed: user input
    :param old_letters_guessed: previous inputs
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True if input is valid, False if not.
    :rtype: boolean
    """

    return len(letter_guessed) == 1 and letter_guessed.isalpha() \
           and not letter_guessed.lower() in old_letters_guessed
'''


# def main():

#     old_letters = ['a', 'b', 'c']

#     print(old_letters)

#     check_valid_input("A", old_letters)

    

#     print(func.__doc__)           
#     help(func)

    
# if __name__ == "__main__":
#     main()



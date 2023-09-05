def is_valid_input(letter_guessed):
    '''
    Checks the validation of input (character)
    :param: letter_guessed: user guess 
    :type: string
    :return: Whether or not the input was valid
    :rtype: boolean
    '''
    
    if len(letter_guessed) > 1:
        return False 

    elif letter_guessed.isalpha():
        return True

    return False


'''
def is_valid_input(letter_guessed):
    """Checks the validation of input (character)
    :param: letter_guessed: userâ€™s guess
    :type: string
    :return: Whether or not the input was valid
    :rtype: boolean
    """
    char = letter_guessed
    if len(char) == 1 and char.isalpha():
        return True
    else:
        return False
        
'''
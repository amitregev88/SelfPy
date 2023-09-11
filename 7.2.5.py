def sequence_del(my_str):

    no_sequence = []

    for letter in my_str:
        if letter not in no_sequence:
            no_sequence.append(letter)

    output_str = "".join(no_sequence)
    return output_str


def sequence_del(my_str):
    """Deletes all letter duplicates in the input string.
    :param my_str: input string
    :type my_str: string.
    :return: the input string, without duplicates (one letter out of each sequence)
    :rtype: string.
	"""
    if len(my_str) > 0:
        result = my_str[0]
        for char in my_str[1:]:
            if char != result[-1]:
                result = result + char
        return result
    return my_str
def arrow(my_char, max_length):
     
    arrow_output = ''

    line = 1 
    
    if line == max_length:
        return my_char

    
    for line in range(1 ,max_length + 1, 1):
        arrow_output += my_char * line + "\n"



    for line in range(max_length - 1, 0, -1):
        arrow_output += (my_char) * line + "\n"

    return arrow_output[:-1]




# def arrow(my_char, max_length):
#     """
#     Draw an errow-shape, built of the input character.
#     :param my_char: the chararter to nuild the errow with
#     :param max_length: length of the longest raw in the shape
#     :type my_char: character
#     :type max_length: int
#     :return: the errow shape
#     :rtype: list
#     """
#     result = ''
#     for i in range(1, max_length+1):
#         result = result + (my_char * i) + '\n'
#     for i in range(max_length-1, 0, -1):
#         result = result + (my_char * i) + '\n'
#     return result[:-1]

# """
# Checks the function (not neccesary for the solution)
# """
# if __name__ == "__main__":
#     print(arrow('D', 1))
#     print(arrow('*', 5))
def count_chars(my_str):

    str_without_spaces = my_str.replace(" ","")

    to_return = {}

    for char in str_without_spaces:

        if char in to_return:
            to_return[char] += 1

        else:
            to_return[char] = 1
    
    return to_return

# def count_chars(my_str):
#     """Counts the frequency of each char in the input list and builds a 
#     dictionary, contains the char and its freq.
#     :paran: my_str: the input list of characters
#     :type: list
#     :return: a dictionay, in the forman [chat, freq]
#     :rtype: dictionay 
#     """

#     my_dict = {}
#     for c in my_str:
#         if c != ' ':
#             if c in my_dict:
#                 my_dict[c] = my_dict[c] + 1
#             else:
#                 my_dict[c] = 1
#     return my_dict
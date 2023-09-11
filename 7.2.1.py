def is_greater(my_list, n):
    greater_than_n = []
    for num in my_list:
        if num > n:
            greater_than_n.append(num)
    return greater_than_n
            
# def is_greater(my_list, n):
#     """Returns all the numbers in "my_list" which are bigger than "n".
#     :param my_list: a list of numbers.
#     :param n: the number to which "my_list" numbers are compared.
#     :type my_list: list
#     :type n: float
#     :return: list of numbers of â€œmy_listâ€ which are bigger than "n".
#     :rtype: list.
# 	"""

#     return [l for l in my_list if l > n]


# def is_greater(my_list, n):
#     return [ greater_than_n for greater_than_n in my_list if greater_than_n > n]
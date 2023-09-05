def longest(my_list):
    l1 = sorted(my_list, key=len)
    return l1[-1:-2:-1][0]

    
'''
    def longest(my_list):
    """Finds the longest string in a list of strings.
    :param my_list: list of strings
    :type my_list: list
    :return: the longest string in my_list
    :rtype: String
	"""

    return max(my_list, key=len)
'''
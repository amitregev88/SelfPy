def extend_list_x(list_x, list_y):
    list_x = [*list_y, *list_x]
    return list_x


'''
def extend_list_x(list_x, list_y):
    """Gets two lists, appends the second one at the beginning of the first one.
    :param list_x: first list
    :param list_y: second list
    :type list_x: list
    :type list_y: list
    :return: the appended list: [list_y list_x]
    :rtype: list
	"""

    list_x[:0] = list_y
    return list_x
'''
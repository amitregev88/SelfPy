def are_lists_equal(list1, list2):
    l1 = sorted(list1)
    l2 = sorted(list2)
    return l1 == l2
    
    
'''
def are_lists_equal(list1,list2):
    """ Checks if two lists containing ints and floats are equal.
    :param list1: first list
    :param list2: second list
    :type list1: list
    :type list2: list
    :return: True if equal, False if not
    :rtype: boolean
    """
    list1.sort()
    list2.sort()
    return list1==list2
'''
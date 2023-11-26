def inverse_dict(my_dict):
    """ return a new dictionary with original values as key and list of original keys as value
        :param original_dict: any desired dictionary
        :type original_dict:  dict
        :rtype: dict
    """
    out_dict = dict()
    for original_key in my_dict:
        original_value =  my_dict[original_key]
        if original_value in out_dict.keys():
            out_dict[original_value] += [original_key]
            out_dict[original_value].sort()
        else:
            out_dict[original_value] = [original_key]

    return out_dict


# def inverse_dict(my_dict):
#     """cross-changes values and keys in a dictionary: each value becomes a key and
#     each key becomes a value.
#     :paran: my_dict: the input dictionary
#     :type: tuple
#     :return: the cross-changed dictionay
#     :rtype: tuple
#     """

#     new_dict = {}
#     for key in my_dict:
#         if my_dict[key] in new_dict:
#             new_dict[my_dict[key]].append(key)
#         else:
#             new_dict[my_dict[key]] = [key]
#     for key in new_dict:
#         new_dict[key].sort()
#     return new_dict
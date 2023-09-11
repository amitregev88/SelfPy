def squared_numbers(start, stop):

    squared_list = []

    while start <= stop:
        squared_list.append(start**2)
        start+=1
    
    return squared_list
    


# def squared_numbers(start, stop):
#     """Prints all the number between "start" and "stop", squared.
#     :param start: first number in range.
#     :param stop: last number in range, assumed >= "start".
#     :type start: int
#     :type stop: int
#     :return: a list of all numbers between "start" and "stop", squared.
#     :rtype: list.
# 	"""

#     x = []  # the squared values
#     while start <= stop:
#         x.append(start ** 2)
#         start += 1
#     return x

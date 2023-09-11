def seven_boom(end_number):

    seven_list = [*range(end_number + 1)]
   
    for i in range(end_number + 1):
        if i % 7 == 0 or '7' in str(i):
            seven_list[i] = "BOOM"
            
    return seven_list




# def boomify(num):
#     """Checks if a num is a multiple of 7 or contains â€˜7â€™. Returns 'BOOM' if TRUE,
#     num otherwise.
#     :param num: the number to be checked
#     :type num: int
#     returns 'BOOM' or num
#     rtype: int or str
#     """
#     if num % 7 == 0 or '7' in str(num):
#         return 'BOOM'
#     else:
#         return num


# def seven_boom(end_number):
#     """Implements 7-BOOM game: gets a number as an input, returns a list in the
#     range of 0-number in which all numbers that are multiples of 7 or contains â€˜7â€™
#     are replaced by â€œBOOMâ€.
#    	:param end_number: input number
#    	:type end_number: int
#    	returns the list of numbers 0-end_number, with the correct changes
#    	:rtype: list
# 	"""

#     return [boomify(i) for i in range(end_number + 1)]


# def main():

#     print(seven_boom(17))

# if __name__ == "__main__":
#     main()
def numbers_letters_count(my_str):
    numeric  = 0
    for i in my_str:
        if i.isnumeric():
            numeric += 1
        
    return [numeric, len(my_str) - numeric]
            




# def numbers_letters_count(my_str):
#     """Counts number of digits and non-digits in "my_str".
#     :param my_str: input string, contains characters
#     :type my_str: string
#     :return: 2-element list: the first element is the number of digits in â€œmy_strâ€,
#     the second one is the number of non-digit characters in â€œmy_strâ€
#     :rtype: list.
# 	"""

#     digits = [char for char in my_str if char >= '0' and char <= '9']
#     return [len(digits), len(my_str)-len(digits)]



# def main():

#     print(numbers_letters_count("Python 3.6.3"))

# if __name__ == "__main__":
#     main()

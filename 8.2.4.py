
def sort_anagrams(list_of_strings):


    # initializing an empty dict
    grouped_anagrams = {}
    # iterating over the list to group all anagrams
    for string in list_of_strings:

        # sorting the string
        sorted_string = str(sorted(string))

        # checking the string in dict
        if sorted_string in grouped_anagrams:

            # adding the string to the group anagrams
            grouped_anagrams[sorted_string].append(string)

        else:
            # initializing a list with current string
            grouped_anagrams[sorted_string] = [string]
    # return the values of the dict (anagram groups)

    to_return = list(grouped_anagrams.values())
    to_return.sort()

    return to_return


def main():

    list_of_words = ['abc', 'bcd', 'cda']
    print(sort_anagrams(list_of_words))
    

if __name__ == "__main__":
    main()


# def sort_anagrams(list_of_strings):
#     """Splits a list of words into sub-lists, each contains anagrams of words from
#     the original list.
#     :param: list_of_strings: the given list of words
#     :type: list of lists
#     :return: list of anagram-lists
#     :rtype: list of lists
#     """

#     result = []
#     for string in list_of_strings:
#         if set(string) in [set(s[0]) for s in result]:
#             for s in result:
#                 if set(string) == set(s[0]):
#                     s.append(string)
#         else:
#             result.append([string])
#     return result


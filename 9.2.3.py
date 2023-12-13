def who_is_missing(file_name):
    with open(file_name,"r") as input_file:
        nums_list = input_file.read()

    nums_list = [int(ele) for ele in nums_list.split(",")]

    nums_list.sort()

    print(nums_list)
    
    for x in range(1, len(nums_list) + 1):
        if x not in nums_list:           
            with open("found.txt","w") as output_file:
                output_file.write(str(x))
    
    return x



def main():
       
    who_is_missing("nums.txt")
    
if __name__ == "__main__":
    main()


# """Finds a missing number in a sequence of numbers (un-sorted), read from a given file. Writes the missing number to a new file.
# :param: file_name: path of the file contains th numbers
# :type: string
# :return: n: the missing number
# :rtype: int
# """
# def who_is_missing(file_name):
#     fid = open(file_name, "r")
#     line = fid.read()
#     n_list = [int(n) for n in line.split(',')]
#     fid.close()
#     for n in range(1, len(n_list) + 2):
#         if n not in n_list:
#             fout = open("found.txt", "w")
#             fout.write(str(n))
#             return n


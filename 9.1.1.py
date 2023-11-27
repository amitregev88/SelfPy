def are_files_equal(file1, file2):
    
    with open(file1,'r') as f1, \
 	    open(file2,'r') as f2:
    
        return f1.readlines() == f2.readlines()



# """Compares 2 files.
#     :param: file1, file2: path of compared files
#     :type: string
#     :return: True if files equal, False if not
#     :rtype: boolean
# """
# def are_files_equal(file1, file2):
# 	with open(file1,'r') as input_file1, \
# 	     open(file2,'r') as input_file2:
# 			rawData1=input_file1.read()
# 			rawData2=input_file2.read()
# 			if (rawData1==rawData2):
# 				return True
# 			else:
# 				return False
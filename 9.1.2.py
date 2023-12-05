file_path = input("Enter a file path:\n")
act = input("Enter a task: rev, sort or last\n")

fname = open(file_path,"r")

if act == "rev":

    for line in fname: 

        print(line[::-1])
 
elif act == "sort":

    list_without_dup = set((fname.read().split()))
    sort_list = sorted(list_without_dup)
    print(sort_list)
   
elif act == "last":

    num_of_last_lines = input("Enter a number:\n")

    for line in (fname.readlines() [-int(num_of_last_lines):]):
        print(line, end ='')

else:
    print("invalid task\n")

fname.close()


# """Applies manipulations on the contenet of a given file, according to a given command.
# :param: filePath: path of the file to manipulate (user's input)
# :param: Command: the comman to apply. Can be sort/reverse/print last n raws/ (user's input)
# :type filePath: string
# :type Command: int
# """
# filePath = input("Enter file path: ")
# command = input("Enter command: ")
# with open(filePath,'r') as inputFile:
# 	if(command=="sort"):
# 		l=list()
# 		for line in inputFile:
# 			line=line.split()
# 			for word in line:
# 				if(word not in l):
# 					l.append(word)
# 		l.sort()
# 		print (l)
# 	elif(command=="rev"):
# 		for line in inputFile:
# 			print(line[-2::-1])
# 	elif(command=="last"):
# 		fileData=inputFile.read()
# 		l=fileData.split('\n')
# 		num=int(input("Enter real number: "))
# 		for i in range(num):
# 			print(l[-num+i])
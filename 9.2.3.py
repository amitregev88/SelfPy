def who_is_missing(file_name):
    with open(file_name,"r") as input_file:
        nums_list_str = input_file.read()
        print("nanana\n")
        print(nums_list_str)

    nums_list = [eval(i) for i in nums_list_str]
    print(nums_list)
    nums_list.sort()
    
    for x in nums_list:
        if x + 1 - x > 1:
            x +=1
            with open("found.txt","w") as output_file:
                output_file.write(x)
                return x



def main():
       
# run the function
    who_is_missing("nums.txt")
    
    

if __name__ == "__main__":
    main()


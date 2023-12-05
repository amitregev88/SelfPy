def copy_file_content(source, destination):
    with open(source,"r") as input_file:
        to_copy = input_file.read()
    

    with open(destination,"w") as output_file:
        output_file.write(to_copy)


#  def main():

#       copy_file_content("input.txt","output.txt")
    
    

# if __name__ == "__main__":
#     main()


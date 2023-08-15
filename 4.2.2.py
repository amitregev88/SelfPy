input_string = input("Please enter a string:\n")

string = input_string.replace(" ", "").lower()
rev_str = string[-1::-1]

if string == rev_str:
    print("OK\n")
else:
    print("NOT\n")
    

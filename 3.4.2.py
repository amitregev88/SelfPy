str = input("Please enter a string:")

first_letter = str[0]

str2 = str[1:] 


new_str = first_letter + str2.replace(first_letter,"e")

print(new_str)


"""
fix_me = input("Enter a string: ")
first_letter = fix_me[0]
print(first_letter + fix_me[1:].replace(first_letter, 'e'))
"""
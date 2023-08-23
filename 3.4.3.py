str = input("Please enter a string:")

len = len(str)

str1 = str[:(len // 2)]

str1 = str1.lower() 

str2 = str[(len // 2):]

str2 = str2.upper()

print(str1 + str2)

"""
fix_me = input("enter string:")
half = round(len(fix_me)/2)
print(fix_me[:half].lower() + fix_me[half:].upper())
"""
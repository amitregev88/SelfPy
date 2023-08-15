guess_user = input("Guess a letter:\n")

len = len(guess_user)

if len > 1:
    if guess_user.isalpha():
        print("E1")
    else:
        print("E3")

elif guess_user.isalpha():
        
        print(guess_user.lower())

else:
    print("E2")

"""
char = input("Guess a letter:")
right_size = len(char) == 1
is_alpha = char.isalpha()
if right_size and is_alpha:
    print(char.lower())
if not right_size and not is_alpha:
    print("E3")
if not right_size and is_alpha:
    print("E1")
if right_size and not is_alpha:
    print("E2")
    
    """
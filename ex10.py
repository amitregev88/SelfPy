def get_secret_word():
    intput_path = input("Enter file path:")
    word_location_in_file = int(input("Enter index:"))

    with open(intput_path) as file:
        data = file.read()
        words = data.split()

    print("\nLet’s start!\n")

    secret_word = words[word_location_in_file - 1]
    return secret_word

def choose_word(file_path, index):
    with open (file_path, 'r') as words_file:
        words = words_file.readlines()

    word = []
    for line in words:
        word += line.split(" ")

    num_of_words_without_dup = len(set(word))

    to_return = (num_of_words_without_dup, word[(index - 1) % len(word)])

    return to_return
     

def main():
       
    print(choose_word("words.txt",15))
    
if __name__ == "__main__":
    main()
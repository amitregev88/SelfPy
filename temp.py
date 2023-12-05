import random

def hangman():
    word_list = ["python", "java", "hangman", "javascript", "ruby"]
    random_number = random.randint(0, 4)
    chosen_word = word_list[random_number]
    guess_word = []
    for character in chosen_word:
        guess_word.append("_")
    print("The word You need to guess has", len(chosen_word), "characters")
    print(' '.join(guess_word))
    trying = 10

    while trying > 0:
        guess = input("Enter a character: ").lower()
        if guess not in chosen_word:
            trying -= 1
            print("Wrong Guess. You have ", trying, "tries left")
        else:
            for index, char in enumerate(chosen_word):
                if char == guess:
                    guess_word[index] = guess
            print(' '.join(guess_word))

        if "_" not in guess_word:
            print("Congratulations, You won!")
            break

    if trying == 0:
        print("You lost! The word was", chosen_word)

hangman()
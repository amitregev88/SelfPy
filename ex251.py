
def print_opening_screen():

    HANGMAN_ASCII_ART = """

    Welcome to the game Hangman \n\n

     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |
                        |___/
                        """

    MAX_TRIES = 6


    print(HANGMAN_ASCII_ART,"\n",MAX_TRIES)
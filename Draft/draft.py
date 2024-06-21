alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_word() -> str:   
    """
    Function which prompts the chooser player for their word and returns that word.
    :return: The word entered by the chooser player in uppercase.
    """
    return input("mot ? ").upper()

def get_lives() -> int: 
    """
    Function which prompts the chooser player for a number of lives and returns this number of lives.
    :return: The number of lives entered by the chooser player.
    """ 
    nbLife = False
    while type(nbLife) != int:
        try:
            nbLife = int(input("nb life ?"))
            break
        except:
            pass
    return nbLife

def get_guess(suggested_letters: list[str]) -> list[str]:
    """
    Function which takes as argument:
    - suggested_letters: a list of the letters suggested by the guesser player throughout the game
    - get_guess(...) does the following:
        - prompts the user for a letter
        - if user gives more than one letter, prompts again
        - if already suggested letter, prompts again
    :param suggested_letters: List of letters already suggested by the guesser.
    :return: Updated list of suggested letters including the newly guessed letter.
    """
    letter = input("Une lettre svp ? ").upper()
    while len(letter) > 1 or letter not in alpha or letter in suggested_letters:
        letter = input("Une lettre svp ? ").upper()
    suggested_letters.append(letter)
    return suggested_letters

def assess_guess(secret_word: str, guessed_letter: str, lives_left: int) -> int:
    """
    Function which takes as argument:
    - secret_word: the word to be guessed
    - guessed_letter: the last letter suggested from guesser player
    - lives_left: lives left
    - assess_guess(...) does the following:
        - outputs if the guess is correct or not
        - returns the current lives of the player depending on the outcome of the guess
    :param secret_word: The word to be guessed.
    :param guessed_letter: The letter guessed by the player.
    :param lives_left: The number of lives remaining.
    :return: Updated number of lives left after assessing the guess.
    """
    if not guessed_letter in secret_word:
        lives_left -= 1
    return lives_left

def display_word(secret_word: str, suggested_letters: list[str]) -> bool:
    """
    Function which takes as argument:
    - secret_word: the word to be guessed
    - suggested_letters: a list of the letters suggested by the guesser player throughout the game
    - display_word(...) does the following:
        - displays the secret word with white spaces between the letters, hiding the non-guessed letters by replacing them with '_'
    :param secret_word: The word to be guessed.
    :param suggested_letters: List of letters already guessed by the player.
    :return: True if the correct word has been found, False otherwise.
    """
    finded = [letter if letter in suggested_letters else "_" for letter in secret_word]
    print(" ".join(finded))
    return "_" not in finded

def main() -> None:
    """
    Main function to run the game. Initializes the game parameters and controls the game loop.
    """
    suggested_letters = []
    word = get_word()
    life = get_lives()

    while not all(letter in suggested_letters for letter in word) and life > 0:
        suggested_letters = get_guess(suggested_letters)
        life = assess_guess(word, suggested_letters[-1], life)
        display_word(word, suggested_letters)
        print(f"Il vous reste {life} vie(s) !")

    print("GG!") if life > 0 else print("Dommage")

if __name__ == "__main__":
    main()

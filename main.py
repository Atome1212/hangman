from Utils import Hangman
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def goodPrint(myStr:str):
    """
    Method Display the word but with a 'bordure'

    param myStr: the string to add a border to
    """
    print("="*len(myStr))
    print(f"{myStr}")
    print("="*len(myStr))

def main():
    """
    Main method that handles the main game loop
    """ 

    clear_screen()
    Hangman = Hangman("./Data/config.csv")
    
    Hangman.display_Hangman()
    goodPrint(f"{Hangman.correctly_guessed_letters}")
    
    
    while Hangman.start_game():
        clear_screen()

        Hangman.display_Hangman()
        goodPrint(f"{Hangman.correctly_guessed_letters}")
        print(f"Wrong letters : {Hangman.wrongly_guessed_letters}")

        print(str(Hangman.lives) + " " + ("lives" if Hangman.lives > 1 else "life") + " " + "left")
    

if __name__ == "__main__":
    main()

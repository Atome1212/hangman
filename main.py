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
    hungman = Hungman("./Data/config.csv")
    
    hungman.display_hungman()
    goodPrint(f"{hungman.correctly_guessed_letters}")
    
    
    while hungman.start_game():
        clear_screen()

        hungman.display_hungman()
        goodPrint(f"{hungman.correctly_guessed_letters}")
        print(f"Wrong letters : {hungman.wrongly_guessed_letters}")

        print(str(hungman.lives) + " " + ("lives" if hungman.lives > 1 else "life") + " " + "left")
    

if __name__ == "__main__":
    main()

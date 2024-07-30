from typing import List
from random import choice
import time

class Hangman:
    """
    Class representing the Hangman game.
    """

    def __init__(self, link:str|bool):
        """
        Constructor of the class Hangman.

        :param lives: The number of lives the player starts with.
        """
        self.stages = [  # état final : tête, torse, les deux bras, et les deux jambes
                        """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / \\
    -
                        """,
                        # jambe gauche
                        """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / 
    -
                        """,
                        # jambe droite
                        """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |      
    -
                        """,
                        # bras gauche
                        """
    --------
    |      |
    |      O
    |     \\|/
    |      
    |     
    -
                        """,
                        # bras droit
                        """
    --------
    |      |
    |      O
    |     \\|
    |      
    |     
    -
                        """,
                        # torse
                        """
    --------
    |      |
    |      O
    |      |
    |      
    |     
    -
                        """,
                        # tête
                        """
    --------
    |      |
    |      O
    |    
    |      
    |     
    -
                        """,
                        # état initial
                        """
    --------
    |      |
    |      
    |    
    |      
    |     
    -
                        """
        ]
        
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions', 'loic'] if not link else self.config_file(link)
        self.word_to_find: List[str] = list(choice(self.possible_words))
        self.lives: int = len(self.stages)-1
        self.correctly_guessed_letters: List[str] = ["_" for _ in range(len(self.word_to_find))]
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    @property
    def get_word_to_find(self) -> str:
        """
        Method return the word to find

        :return word_to_find: the word to find
        """
        return str(self.word_to_find)

    def config_file(self, link:str) :
        """
        Method to read the config file and add all the words to the possible_words list.

        :param link: The path to the configuration file.
        """
        configList:List[str] = []

        with open(link) as my_file:
            content = my_file.read()
            configList = content.split(",\n")

        return configList


    def play(self) -> None:
        """
        Method to play one turn of the game.
        Prompts the user to enter a letter and updates the game state based on the guess.
        """
        letter: str = input("Enter a letter: ")

        while not letter.isalpha() or len(letter) != 1 or letter in self.wrongly_guessed_letters or letter in self.correctly_guessed_letters:
            print("Error")
            letter = input("Enter a letter: ")

        if letter.lower() in self.word_to_find:
            for j, i in enumerate(self.word_to_find):
                if i == letter.lower():
                    self.correctly_guessed_letters[j] = i
        else:
            self.wrongly_guessed_letters.append(letter.lower())
            self.error_count += 1
            self.lives -= 1

        self.turn_count += 1

    def start_game(self) -> bool:
        """
        Method to start and manage the game loop.
        Checks if the game is over or if the word is found and continues the game if neither condition is met.

        :return: False if the game is over or the word is found, True otherwise.
        """
        if self.lives <= 0:
            self.game_over()
            return False
        elif self.correctly_guessed_letters == self.word_to_find:
            self.well_played()
            return False
        else:
            self.play()
            return True
        
    def display_hangman(self) -> None:
        """
        Method display the hangman
        """
        print(self.stages[self.lives])

    def game_over(self) -> None:
        """
        Method to be called when the game is over.
        Prints a game over message.
        """
        print(f"Game over... the word was {self.get_word_to_find}")

    def well_played(self) -> None:
        """
        Method to be called when the player has successfully guessed the word.
        Prints a congratulatory message with the number of turns and errors.
        """
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")

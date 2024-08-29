
# 🎮 Hangman Game README

![Hangman Game Demo](https://mgsrizqi.com/my-games/hangmangame/sprites/7.gif)

## 🔣 Language
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)

## 📑 Table of Contents
1. [Introduction](#introduction)
2. [Class: Hangman](#class-hangman)
   - [Attributes](#attributes)
   - [Methods](#methods)
3. [Additional Functions](#additional-functions)
4. [How to Run the Game](#how-to-run-the-game)
5. [Game Flow](#game-flow)
6. [Conclusion](#conclusion)
7. [Project Tree](#project-tree)

## Introduction

This document provides an overview of the Hangman game implemented in Python. The game allows a user to guess a hidden word one letter at a time, with a limited number of incorrect guesses before the game ends.

## Class: Hangman

The `Hangman` class encapsulates the functionality and state of the Hangman game.

### 📝 Attributes

- `stages`: A list of strings representing the hangman stages as the player makes incorrect guesses.
- `possible_words`: A list of possible words to be guessed. By default, it contains a preset list of words, but it can be initialized with words from a configuration file.
- `word_to_find`: The word that the player needs to guess, chosen randomly from `possible_words`.
- `lives`: The number of incorrect guesses allowed (initialized to the number of stages minus one).
- `correctly_guessed_letters`: A list of the correctly guessed letters, with initially all positions set to `_`.
- `wrongly_guessed_letters`: A list of the letters guessed incorrectly.
- `turn_count`: The number of turns taken by the player.
- `error_count`: The number of incorrect guesses made by the player.

### 🔍 Methods

- `__init__(self, link: str | bool)`: Initializes the game. If `link` is `True`, it loads words from the specified configuration file.
- `get_word_to_find(self) -> str`: Returns the word to find as a string.
- `config_file(self, link: str) -> List[str]`: Reads a configuration file to add words to the `possible_words` list.
- `play(self) -> None`: Prompts the user to enter a letter and updates the game state based on the guess.
- `start_game(self) -> bool`: Manages the game loop, checking if the game is over or the word is found.
- `display_hangman(self) -> None`: Displays the current state of the hangman.
- `game_over(self) -> None`: Called when the game is over, prints a game over message.
- `well_played(self) -> None`: Called when the player guesses the word, prints a congratulatory message.

## 🛠️ Additional Functions

- `goodPrint(myStr: str)`: Prints a string with a border.
- `main()`: The main function that handles the game loop, initializes the `Hangman` class, and manages the game flow.

## 🖥️ How to Run the Game

1. Ensure you have a Python environment set up.
2. Place the script in a directory.
3. Ensure you have a configuration file `config.csv` in the `./Data/` directory if you want to initialize the game with specific words. The file should contain words separated by commas.
4. Run the script using the command:
   ```bash
   python hangman.py
   ```

## 🔄 Game Flow

1. The game initializes and chooses a random word from the list of possible words.
2. The player is prompted to guess a letter.
3. The game updates the state based on whether the guess is correct or incorrect.
4. The game continues until the player either guesses the word or runs out of lives.
5. The game displays the hangman state and the correctly guessed letters after each guess.

## 🏁 Conclusion

This Hangman game provides a simple yet interactive way to enjoy the classic word-guessing game. It can be customized with different words via a configuration file and includes various features to enhance the gameplay experience.

## 👥 Author

**👷‍♂️ [Atome1212](https://github.com/Atome1212)**: Data Engineer

## 🌳 Project Tree

```
├── Data
│   └── config.csv
├── Draft
│   └── draft.py
├── README.md
├── Utils
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── game.cpython-310.pyc
│   │   └── game.cpython-311.pyc
│   └── game.py
└── main.py
```

This tree provides an overview of the project structure, showing where each file and directory is located.

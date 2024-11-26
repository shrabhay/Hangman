# Hangman Game
## Description
The Hangman Game is a fun and interactive word-guessing game implemented in Python. The player attempts to guess the letters of a hidden word within a limited number of guesses. With visual feedback and an engaging word bank, this project offers a classic gaming experience.

---

## Features
* Randomly selects a word from a predefined list.
* Provides visual feedback for the hangman figure as incorrect guesses are made.
* Tracks correctly and incorrectly guessed letters.
* Offers a user-friendly and interactive terminal-based gameplay.

---

## Files Included
* `hangman_the_game.py`: The main script that handles the game logic and user interaction.
* `hangman_words.py`: Contains the word list from which the hidden word is randomly selected.
* `hangman_art.py`: Contains ASCII art to visually represent the hangman as the game progresses.

---

## Prerequisites
Python 3.x installed on your system.

---

## How to Run
1. Clone or download this repository to your local machine:
    ```shell
    git clone https://github.com/shrabhay/Hangman.git
    cd hangman-game
    ```

2. Run the main script to start the game:
    ```shell
    python3 hangman_the_game.py
    ```

---

## How to Play
1. The game randomly selects a hidden word.
2. You will have a limited number of guesses to uncover the word.
3. On each turn:
   * Enter a letter as your guess.
   * Correct guesses reveal the letter in the word.
   * Incorrect guesses add to the hangman figure.
4. The game ends when:
   * You correctly guess the word.
   * The hangman figure is completed (you lose).

---

## Example Gameplay
```
Welcome to Hangman!
_ _ _ _ _

Guess a letter: e
Correct!

e _ _ _ e

Guess a letter: x
Wrong! 5 guesses left.

    +---+
    O   |
        |
        |
       ===

Guess a letter: a
...
```

---

## Future Enhancements
* Add difficulty levels (e.g., easy, medium, hard).
* Enhance the word bank with more categories.
* Implement a graphical user interface (GUI) for broader accessibility.
* Allow multiplayer functionality for competitive gameplay.

---

## License
This project is open-source and available under the MIT License.

---

## Contributing
Contributions are welcome! If you have ideas for improvements, feel free to fork this repository and submit a pull request.
1. Fork the repository.
2. Create a new branch:
    ```shell
    git checkout -b feature-name
    ```

3. Make your changes and commit them:
    ```
    git commit -m "Add feature-name"
    ```

4. Push to your branch:
    ```shell
    git push origin feature-name
    ```

5. Open a pull request.

# Wordle game

A Wordle-inspired word guessing game developed in Python using the Tkinter library. The game provides a graphical interface where players attempt to guess a randomly selected five-letter word within six attempts.

## Current Features

- Graphical user interface built with Tkinter
- Randomly selects a five-letter word from a predefined word list
- Six-row game board
- Five-letter guesses
- Keyboard input support
- On-screen keyboard
- Color-based feedback for guessed letters
- Displays correct letters in the correct position
- Identifies letters that exist in the word but are in the wrong position
- Identifies letters that are not present in the secret word

## Technologies Used

- Python
- Tkinter
- Random module

## How It Works

At the beginning of each game, the program randomly selects a five-letter word from a predefined list.

The player enters a five-letter guess using either the physical keyboard or the on-screen keyboard. After pressing Enter, the program compares the guess with the secret word.

The game provides visual feedback for each letter:

- Green — correct letter in the correct position
- Gold — correct letter but in the wrong position
- Gray — letter is not present in the secret word

The player has a maximum of six attempts to guess the secret word.

## How to Run

Make sure Python is installed on your system.

Run the following command:

```bash
python wordle_game.py

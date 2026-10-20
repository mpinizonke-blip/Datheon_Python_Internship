# Hangman Word Guessing Game

A simple terminal-based Hangman game built with Python. 

## How to Play
1. Download `hangman.py` and `english_words.txt` into the same folder.
2. Open your command line interface (Terminal or PowerShell) inside that folder.
3. Run the game by typing:
   ```bash
   python hangman.py
   ```

## Features
- Dynamic ASCII gallows art that updates with each incorrect guess.
- Automatically reads a custom list of words from `english_words.txt`.
- Smart input check prevents losing lives when guessing duplicate letters.

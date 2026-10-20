import random
import os

STAGES = [
    "\n  --------\n  |      |\n  |\n  |\n  |\n  |\n- - - - -",
    "\n  --------\n  |      |\n  |      O\n  |\n  |\n  |\n- - - - -",
    "\n  --------\n  |      |\n  |      O\n  |      |\n  |      |\n  |\n- - - - -",
    "\n  --------\n  |      |\n  |      O\n  |     /|\n  |      |\n  |\n- - - - -",
    "\n  --------\n  |      |\n  |      O\n  |     /|\\\n  |      |\n  |\n- - - - -",
    "\n  --------\n  |      |\n  |      O\n  |     /|\\\n  |      |\n  |     /\n- - - - -",
    "\n  --------\n  |      |\n  |      O\n  |     /|\\\n  |      |\n  |     / \\\n- - - - -"
]

def load_words():
    """Loads and filters words from the repository text file."""
    filename = "english_words.txt"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            words = [line.strip().upper() for line in f if len(line.strip()) >= 4 and line.strip().isalpha()]
        if words:
            print(f"📦 Successfully loaded {len(words)} words from '{filename}'!")
            return words
    
    print("⚠️ File 'english_words.txt' not found or empty. Using internal backup list.")
    return ["PYTHON", "DEVELOPER", "INTERNSHIP", "PORTFOLIO"]

def play_game(word_list):
    secret_word = random.choice(word_list)
    guessed_letters = set()
    errors = 0
    max_errors = 6

    print("\n" + "="*40)
    print("      WELCOME TO DATHEON HANGMAN       ")
    print("="*40)

    while errors < max_errors:
        print(STAGES[errors])
        
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Guesses: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining Lives: {max_errors - errors}")
        print("-" * 40)

        if "_" not in display_word:
            print(r"🎉 VICTORY! You guessed the word: " + secret_word + "\n")
            return

        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already tried '{guess}'.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Correct! '{guess}' is in the word.")
        else:
            errors += 1
            print(f"❌ Wrong! '{guess}' is not in the word.")

    print(STAGES[errors])
    print("☠️ GAME OVER! The word was: " + secret_word + "\n")

if __name__ == "__main__":
    words_pool = load_words()
    while True:
        play_game(words_pool)
        if input("Play again? (y/n): ").strip().lower() != 'y':
            print("Goodbye!")
            break
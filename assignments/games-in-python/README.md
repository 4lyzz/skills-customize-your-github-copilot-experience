
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python. The player guesses letters to reveal a randomly selected word before running out of attempts, practicing strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a secret word and initialize the variables needed to track the player's progress.

#### Requirements
Completed program should:

- Randomly select a word from the provided `words` list.
- Track the letters guessed, the number of incorrect guesses, and the maximum number of incorrect guesses.
- Display the word as underscores, revealing letters the player has guessed correctly.

### 🛠️ Run the Guessing Loop

#### Description
Prompt the player to guess letters, update the game state, and finish when the word is guessed or the player runs out of attempts.

#### Requirements
Completed program should:

- Accept one letter per guess and let the player know if that letter has already been guessed.
- Reveal correctly guessed letters and count incorrect guesses toward the attempt limit.
- End with a win message when the player reveals the whole word.
- End with a loss message and reveal the secret word when the attempt limit is reached.

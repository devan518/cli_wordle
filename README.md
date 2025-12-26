
# Wordle in Python

A command-line implementation of the popular word game Wordle.

## Description

This project allows you to play Wordle directly in your terminal. It fetches a random word of a specified length from an API and provides color-coded feedback on your guesses (like the real one).

## Features

- **Dynamic Word Length**: You can choose the length of the word you want to guess (minimum 3 letters).
- **Random Words**: Words are fetched dynamically from the [Random Word API](https://random-word-api.herokuapp.com/).
- **Visual Feedback**: Uses `colorama` to provide colored output similar to the original game:
  - **Green**: Correct letter, correct spot.
  - **Yellow**: Correct letter, wrong spot.
  - **Grey**: Letter not in the word.

    Expect updates Soon! Next update: /hint command and ai api for checking if the word given is too easy.

## Installation:
### Prerequisites

- Python 3.x
- Internet connection (for fetching words)



1. Clone the repository or download the source code.
2. Install the required Python packages:

   ```bash
   pip install colorama requests
   ```
However, this is not reccommended for beginners so, i will package a .exe file in
later updates.

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. When prompted, enter the number of letters for the wordle (minimum 3).
3. The game will start. Type your guesses and press Enter.
4. You have 6 attempts to guess the word.

## Disclaimer

The program uses an external API for word generation. Occasionally, it may select obscure or difficult words.

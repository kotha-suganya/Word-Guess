🎮 Word Guessing Game (Python)

A simple command-line Word Guessing Game built using Python.
The program randomly selects a word from a file and the player must guess the word one letter at a time within a limited number of chances.

The game provides hints by showing underscores for hidden letters and reveals them as the player guesses correctly.

📌 Features

🎲 Random word selection from a word list

🔤 Letter-by-letter guessing

⏳ Limited number of chances

✔ Input validation (only single alphabet allowed)

🔁 Prevents repeated guesses

🎉 Win and lose messages

🛑 Graceful exit using Ctrl + C

🛠️ Technologies Used

Python

random module

collections.Counter

📂 Project Structure
word-guess-game
│
├── game.py        # Main Python game file
├── words.txt      # List of words used in the game
└── README.md      # Project documentation
▶️ How to Run

Clone the repository

git clone https://github.com/yourusername/word-guess-game.git

Navigate to the project folder

cd word-guess-game

Run the Python file

python game.py
📄 Example Gameplay
Guess the word!
_ _ _ _ _

Enter a letter to guess: a
Good job! Correct guess 👍

_ a _ _ _
🎯 Learning Purpose

This project helps beginners understand:

Python loops

Conditional statements

File handling

String manipulation

Basic game logic

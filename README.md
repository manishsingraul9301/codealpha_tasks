<h1>🎯 Hangman Game (Text-Based)</h1>
<h2>📌 Project Overview</h2>
<p>
This project is a <b>simple text-based Hangman game</b> built using Python. The player tries to guess a hidden word one letter at a time within a limited number of incorrect attempts.
</p>

<h2>🎯 Goal</h2>
<ul>
  <li>Select a random word from a predefined list</li>
  <li>Allow the player to guess letters one by one</li>
  <li>Limit incorrect guesses to <b>6 attempts</b></li>
  <li>End the game when the word is guessed or attempts run out</li>
</ul>

<h2>🧠 Key Concepts Used</h2>
<ul>
  <li>random module</li>
  <li>while loop</li>
  <li>if-else conditions</li>
  <li>Strings and Lists</li>
  <li>User input/output</li>
</ul>

<h2>⚙️ How It Works</h2>
<ol>
  <li>A random word is selected from a list of 5 words.</li>
  <li>The word is hidden using underscores (_).</li>
  <li>The player guesses letters one by one.</li>
  <li>Correct guesses reveal letters in the word.</li>
  <li>Incorrect guesses reduce remaining attempts.</li>
  <li>Game ends when:
    <ul>
      <li>Word is guessed ✅</li>
      <li>Attempts reach zero ❌</li>
    </ul>
  </li>
</ol>

<h2>💬 Example Gameplay</h2>
<pre>
Word: _ _ _ _

Guess a letter: a
Wrong guess! Attempts left: 5

Guess a letter: e
Correct!

Word: _ e _ e

Guess a letter: l
Correct!

Word: _ e l e

Guess a letter: p
Correct!

🎉 You guessed the word: help
</pre>

<h2>📂 Project Structure</h2>
<pre>
hangman-game/
│
├── hangman.py
└── README.md
</pre>

<h2>▶️ How to Run</h2>
<ol>
  <li>Make sure Python is installed</li>
  <li>Download or clone the project</li>
  <li>Open terminal in the project folder</li>
  <li>Run the command:</li>
</ol>

<pre>
python hangman.py
</pre>

<h2>🧩 Sample Code</h2>
<pre><code>
import random

words = ["apple", "table", "chair", "plant", "light"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    letter = input("Guess a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if "_" not in guessed:
    print("🎉 You guessed the word:", word)
else:
    print("❌ Game Over! The word was:", word)
</code></pre>

<h2>🚀 Future Improvements</h2>
<ul>
  <li>Add difficulty levels</li>
  <li>Show guessed letters</li>
  <li>Add ASCII hangman drawing</li>
  <li>Allow full word guesses</li>
  <li>Add scoring system</li>
</ul>

<h2>📚 Learning Outcome</h2>
<ul>
  <li>Understanding loops in games</li>
  <li>Working with strings and lists</li>
  <li>Random word selection</li>
  <li>Handling user input</li>
</ul>

<h2>👨‍💻 Author</h2>
<p>Sushil Singraul</p>


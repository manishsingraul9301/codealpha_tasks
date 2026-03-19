import random

def play_hangman():
    # Predefined list of words
    words = ['PYTHON', 'PROGRAM', 'COMPUTER', 'KEYBOARD', 'MONITOR']
    
    # Select a random word
    secret_word = random.choice(words)
    
    # Game state
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    # Create the initial display (all underscores)
    display_word = ['_' for _ in secret_word]
    
    print("=" * 40)
    print("Welcome to Hangman!")
    print("=" * 40)
    print(f"The word has {len(secret_word)} letters.")
    
    # Main game loop
    while incorrect_guesses < max_incorrect:
        # Display current progress
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Incorrect guesses ({incorrect_guesses}/{max_incorrect}): {', '.join(guessed_letters)}")
        
        # Get player's guess
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        # Add to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is in the word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word!")
            
            # Update display word
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess
            
            # Check if player has won
            if '_' not in display_word:
                print(f"\nCongratulations! You guessed the word: {secret_word}")
                print(f"You had {incorrect_guesses} incorrect guesses.")
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            
            # Show hangman progress
            print(f"Remaining guesses: {max_incorrect - incorrect_guesses}")
    
    # Game over messages
    if incorrect_guesses >= max_incorrect:
        print(f"\nGame Over! You've used all {max_incorrect} guesses.")
        print(f"The word was: {secret_word}")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes' or play_again == 'y':
        play_hangman()

# Start the game
if __name__ == "__main__":
    play_hangman()
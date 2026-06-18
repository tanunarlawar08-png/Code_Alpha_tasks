import random

# List of words to guess
words = ['python', 'hangman', 'programming', 'internship', 'computer']

# Pick a random word
word = random.choice(words)

# Initialize game variables
guessed_letters = []
correct_letters = []
wrong_count = 0
max_wrong = 6

print("=" * 40)
print("HANGMAN GAME")
print("=" * 40)
print(f"\nThe word has {len(word)} letters.\n")

# Main game loop
while wrong_count < max_wrong:
    
    # Display current word state
    display_word = ""
    for letter in word:
        if letter in correct_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"Word: {display_word}")
    print(f"Guessed: {guessed_letters}")
    print(f"Wrong guesses: {wrong_count}/{max_wrong}\n")
    
    # Check if player won
    if all(letter in correct_letters for letter in word):
        print("Congratulations! You won! 🎉")
        print(f"The word was: {word}")
        break
    
    # Get user input
    guess = input("Guess a letter: ").lower()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!\n")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue
    
    # Add to guessed letters
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess in word:
        correct_letters.append(guess)
        print(f"Good! '{guess}' is in the word.\n")
    else:
        wrong_count += 1
        print(f"Wrong! '{guess}' is not in the word.\n")

else:
    # Player lost
    print("Game Over! You lost! 😢")
    print(f"The word was: {word}")

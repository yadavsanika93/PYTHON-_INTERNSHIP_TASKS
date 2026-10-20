import random

# ASCII Art for the 6 stages of the gallows (0 to 6 mistakes)
GALLOWS_STAGES = [
    """
       +---+

       |   |
           |
           |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
           |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |

       |   |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|   |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      /    |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    """
]

# Word list for the game
WORD_LIST = ["PYTHON", "DATHEON", "INTERNSHIP", "DEVELOPER", "PROGRAMMING", "CHATBOT", "TERMINAL"]

def display_game_status(word, guessed_letters, mistakes):
    """Displays the gallows, the masked secret word, and the guessed letters."""
    print(GALLOWS_STAGES[mistakes])
    
    # Create the masked string (e.g., _ A _ H E O N)
    masked_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"Word to guess: {masked_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Remaining attempts: {6 - mistakes}")
    print("-" * 30)

def main():
    print("=======================================")
    print("   WELCOME TO HANGMAN (CONSOLE GAME)   ")
    print("=======================================")
    
    # 1. Select a secret word randomly
    secret_word = random.choice(WORD_LIST).upper()
    
    # 2. Initialize tracking variables
    guessed_letters = set()
    unique_secret_letters = set(secret_word)
    mistakes = 0
    max_mistakes = 6

    # 3. Game loop
    while mistakes < max_mistakes:
        display_game_status(secret_word, guessed_letters, mistakes)
        
        # Check for victory condition
        if unique_secret_letters.issubset(guessed_letters):
            print("\n🎉 CONGRATULATIONS! VICTORY! 🎉")
            print(f"You successfully guessed the word: {secret_word}\n")
            return

        # Prompt for user input
        guess = input("Guess a letter: ").strip().upper()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single alphabetical letter.\n")
            continue
            
        # Prevent duplicate penalty deduction
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.\n")
            continue

        # Add to guessed letters set
        guessed_letters.add(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            mistakes += 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.\n")

    # 4. Defeat condition if loop ends without victory
    display_game_status(secret_word, guessed_letters, mistakes)
    print("\n💀 GAME OVER! DEFEAT! 💀")
    print(f"You ran out of attempts. The secret word was: {secret_word}\n")

if __name__ == "_main_":
    main()
import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None
    
    print("Welcome to the Guessing Game!")
    print("I have picked a number between 1 and 100. Try to guess it!")

    # Continue looping until the user guesses the correct number
    while guess != secret_number:
        # Prompt the user to input their guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the attempt counter
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
        except ValueError:
            print("Please enter a valid integer.")

# Start the game
guessing_game()

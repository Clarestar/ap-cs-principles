from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome! to the number-guessing game.'

if __name__ == '__main__':
    app.run(host='localhost', port=7071)


import random 

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1,100)

    # Set the number of attempts
    max_attempts = 5
    attempts = 0 

    # Game loop
    while attempts < max_attempts:
         # Prompt the user to guess the number
        user_guess = int(input("Guess the number (between 1 and 100):"))

        # Check if the guess is correct
        if user_guess == secret_number:
            print("Congratulations! You guessed the right number.")
        else:
            if user_guess < secret_number:
                print("Please try again, the number is higher than the correct answer.")
            else:
                print("Please try again, the number is lower than the answer.")
            
        # Increment the attempts
        attempts += 1

    # Inform the user if they couldn't guess the number in the allowed attempts
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}")

# Run the game
number_guessing_game()
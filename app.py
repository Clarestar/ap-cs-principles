from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome! to the number-guessing game.'

if __name__ == '__main__':
    app.run(host='localhost', port=7071)

import random 

def number_guessing_game():
    secret_number = random.randint(1,100)
    secret_number = (61)
    
    max_attempts = 5
    attempts = 0 

    while attempts < max_attempts:
        user_guess = int(input("Guess the number (between 1 and 100):"))

        if user_guess == secret_number:
            print("Congratulations! You guessed the right number.")
        else:
            if user_guess < secret_number:
                print("Please try again, the correct number is higher than this number.")
            else:
                print("Please try again, the correct number is lower than this number.")
            
        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
    
number_guessing_game()
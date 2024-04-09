import random
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome! to the number-guessing game.'

@app.route('/guess', methods = ['GET', 'POST'])
def number_guessing_game():
    secret_number = random.randint(1, 100)
    print('secret number: ' + str(secret_number))
    
    max_attempts = 5
    attempts = 0 

    if request.method == 'GET':
        return render_template('guess.html', response = '')
    
    if request.method == 'POST':
        guess = request.form['text']
        print(guess)

        if int(guess) < secret_number:
            return render_template('guess.html', response = 'your guess is too low!')
        else: 
            return render_template('guess.html', response = 'your guess is too high!')
    

    # while attempts < max_attempts:
    #     user_guess = int(input("Guess the number (between 1 and 100):"))

    #     if user_guess == secret_number:
    #         print("Congratulations! You guessed the right number.")
    #     else:
    #         if user_guess < secret_number:
    #             print("Please try again, the correct number is higher than this number.")
    #         else:
    #             print("Please try again, the correct number is lower than this number.")
            
    #     attempts += 1

    # if attempts == max_attempts:
    #     print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == '__main__':
    app.run(host='localhost', port=7071)
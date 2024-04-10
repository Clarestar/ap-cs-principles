from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome! to the number-guessing game.'

@app.route('/guess', methods=['GET', 'POST'])
def number_guessing_game():
    if request.method == 'GET':
        secret_number = random.randint(1, 100)
        print('Secret number:', secret_number)
        return render_template('guess.html', response='', message='Guess the number between 1 and 100!')
    
    if request.method == 'POST':
        guess = int(request.form['guess'])
        secret_number = int(request.form['secret_number'])
        attempts = int(request.form['attempts'])
        max_attempts = 5

        if guess == secret_number:
            message = 'Congratulations! You guessed the correct number.'
            return render_template('guess.html', response='success', message=message)

        attempts += 1
        if attempts >= max_attempts:
            message = 'Game over! The secret number was {secret_number}.'
            return render_template('guess.html', response='game_over', message=message)

        if guess < secret_number:
            response = 'Your guess is too low!'
        else:
            response = 'Your guess is too high!'
        
        return render_template('guess.html', response = '')

    # max_attempts = 5
    # attempts = 0 

    # if request.method == 'GET':
    #     return render_template('guess.html', response = '')
    
    # if request.method == 'POST':
    #     guess = request.form['text']                                                                                     
    #     print(guess)

    #     if int(guess) < secret_number:
    #         return render_template('guess.html', response = 'your guess is too low!')
    #     else: 
    #         return render_template('guess.html', response = 'your guess is too high!')
    

    # # while attempts < max_attempts:
    # #     user_guess = int(input("Guess the number (between 1 and 100):"))

    # #     if user_guess == secret_number:
    # #         print("Congratulations! You guessed the right number.")
    # #     else:
    # #         if user_guess < secret_number:
    # #             print("Please try again, the correct number is higher than this number.")
    # #         else:
    # #             print("Please try again, the correct number is lower than this number.")
            
    # #     attempts += 1

    # # if attempts == max_attempts:
    # #     print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == '__main__':
    app.run(host='localhost', port=7071)
    app.run(debug=True)
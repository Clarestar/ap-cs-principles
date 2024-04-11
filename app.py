from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)

@app.route('/')
def hello_world():
    return 'Welcome! to the number-guessing game.'

@app.route('/reset')
def reset():
    global secret_number 
    secret_number = random.randint(1, 100)
    return 'A new secret number has been generated.'

@app.route('/guess', methods=['GET', 'POST'])
def number_guessing_game():
    if request.method == 'GET':
        print('Secret number:', secret_number)
        return render_template('guess.html', response='')
    
    if request.method == 'POST':
        guess = int(request.form['text'])

        if guess == secret_number:
            message = 'Congratulations! You guessed the correct number.'
            return render_template('guess.html', response='success')

        if guess < secret_number:
            response = 'Your guess is too low, Please try again!'
        else:
            response = 'Your guess is too high, Please try again!'
        return render_template('guess.html', response = response)

if __name__ == '__main__':
    app.run(host='localhost', port=7071)
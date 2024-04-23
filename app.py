from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)
secret_numbers = []

def guess_number_list(guess: int, secret_numbers: list[int]) -> str:
    for number in secret_numbers:
        if number == guess:
            return str(guess) + ' is a secret number, you win!'
    return str(guess) + ' is not a secret number, you lose!'

def create_secret_numbers():
    global secret_numbers
    secret_numbers = []
    for i in range(10):
        secret_numbers.append(random.randint(1, 100))

# generate first set of secret numbers
create_secret_numbers()

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
            return render_template('guess.html', response='Congratulations! You guessed the correct number')

        if guess < secret_number:
            response = 'Your guess is too low, Please try again!'
        else:
            response = 'Your guess is too high, Please try again!'
        return render_template('guess.html', response = response)
    
@app.route('/secret_numbers', methods = ['GET', 'POST'])
def guess_secret_numbers():
    if request.method == 'GET':
        print('secret numbers: ' + str(secret_numbers))
        return render_template('guess.html', response='')
    
    if request.method == 'POST':
        guess = int(request.form['text'])
        return guess_number_list(guess, secret_numbers)

if __name__ == '__main__':
    app.run(host='localhost', port=7071)
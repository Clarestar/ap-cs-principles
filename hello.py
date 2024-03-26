import random 

number = random.randint(1,100)
guess = 0

while guess != number:
    guess = int(input("Enter Guess Number: "))
    if (guess < number):
        print("Please try again, the number is lower than the correct answer")
    elif (guess > number):
        print ("Please try again, the number is higher than the correct answer")
    else:
        print ("Congratulations! You get the correct answer")




import random 

def number_guessing_game():
    secret_number = random.randint(1,100)

    max_attempts = 5
    attempts = 0 

    while attempts < max_attempts:
        user_guess = int(input("Guess the number (between 1 and 100):"))

        if user_guess == secret_number:
            print("Congratulations! You guessed the right number.")
        else:
            if user_guess < secret_number:
                print("Please try again, the number is higher than the correct answer.")
            else:
                print("Please try again, the number is lower than the answer.")
            
        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {61}.")

number_guessing_game()
    
import random

number_to_guess = random.randint(1, 20)

max_attempts = 3
attempts = 0

print("Welcome to Guess the Number!")
print("I have selected a number between 1 and 20. Try to guess it!")


while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
    attempts += 1

    
    if guess == number_to_guess:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

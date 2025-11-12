import random


random_number = random.randint(1, 10)


user_choice = int(input("Guess a number between 1 and 10: "))


if user_choice == random_number:
    print(" Congratulations! You guessed it right.")
else:
    print(f" Oops! Wrong guess. The correct number was {random_number}.")

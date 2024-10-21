#Periods 1-2 Aliyah Pargan 10/21/2024
#CFU10

import random
attempts = 0


print("Generate a random number between 1 and 10: ")
num_random = random.randint(1,10)


def attempts(attempts, user_guess)
user_guess = int(input("Guess a number between 1 and 10"))
if user_guess == num_random:
    print("Attempts used: " + str(attempts))
elif user_guess < num_random:
    print("Guess too low, try again!")
else: 
    print("Guess too high try again!")

#period 1-2 Aliyah Pargan    10/17/2024
#CFU9, which is a CFU using import random and if statements. We are basically creating a game where the user can 
#select how many rolls they want, with each roll, a random number would be selected and the user must guess 
#what the number is. 


num_rolls = int(input("How many rolls do you want to play?"))

import random
rolls = random.randint(1,6)
user_guess = int(input("What number do you guess?"))

print(rolls)

if user_guess == rolls:
    print("Congrats! You guessed right! 6+ points")
else: 
    print("Sorry, that wasn't the number... -1 point")

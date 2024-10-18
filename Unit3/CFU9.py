#period 1-2 Aliyah Pargan    10/17/2024
#CFU9, which is a CFU using import random and if statements. We are basically creating a game where the user can 
#select how many rolls they want, with each roll, a random number would be selected and the user must guess 
#what the number is. 


num_rolls = int(input("How many rolls do you want to play?"))
print("Amount of rolls: ", num_rolls)

score = 0
import random
for roll in range(1, num_rolls + 1 ): #loop used to help code work (from w3schools)
    rolls = random.randint(1,6)
    user_guess = int(input(f"Roll {roll}: Guess a number between 1 and 6: "))
    if user_guess == rolls:
        print("Congrats! You guessed right! 6+ points")
        score += 6 #adds points
    else:
        print("Sorry, that wasn't the number... -1 point")
        score -= 1 #subtracts points
        
print("Your final score is: " + str(score))

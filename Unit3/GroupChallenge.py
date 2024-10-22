import random
import math 
total_attempts = 0


print("Generate a random number between 1 and 10: ")
num_random = random.randint(1,10)
num_rounds = int(input("How many rounds do you want to play?"))
user_guess = int(input("Guess a number between 1 and 10"))

def guess(num_random, user_guess):
    print(num_random)
    if user_guess == num_random:
        return total_attempts
    elif user_guess < num_random:
        print("Guess too low, try again!")
    else: 
        print("Guess too high, try again!")
        
def attempts(user_guess,total_attempts =0):
    if user_guess < num_random:
        print("Guess too low, try again!")
        total_attempts = total_attempts + 1
    else:
        print("Guess too high, try again!")
        total_attempts = total_attempts + 1
    
average = total_attempts // num_rounds

total_attempts =attempts(total_attempts)
print(f"total attempts used: {total_attempts}")
print("Average of your score: " + str(average))

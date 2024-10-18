#period 1-2 Aliyah Pargan    10/17/2024
#CFU9, which is a CFU using import random and if statements. We are basically creating a game where the user can 
#select how many rolls they want, with each roll, a random number would be selected and the user must guess 
#what the number is. 


import random
print("Let's roll the dice!")
num_rolls = int(input("How many times do we want to roll the dice?"))

def guess(num_random,total):
    
    guess = int(input("Guess the roll: "))
    if guess == num_random:
        total = total +6
    else:
        total = total -1
        
        
def rolls(num_rolls, total =0):
    num_random = random.randint(1,6)
    if num_rolls ==0:
        return total
    else:
        num_rolls = num_rolls -1
        guess(num_random,total)
        print(f"you roll a {num_random}!")
        return rolls(num_rolls,total)
    
total =rolls(num_rolls)
print(f"total is: {total}")


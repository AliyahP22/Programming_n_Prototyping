#Periods 1-2 Aliyah Pargan 10-22-2024
#Advanced Group challenge, which are elevations of CFU 10: We were to create a guessing game in which a random number would be 
#generated and the user must guess the number until they guess the number correct!.
import random
import time

num_user = int(input("How many rounds do you want to play? "))

total_attempts = 0
round_num = 1
response_time = 0

def difficulty():
    print("\nSelect difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-1000)")
    
    difficulty = int(input("Choose 1, 2, or 3: "))
    
    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 50
    elif difficulty == 3:
        return 1000
    else:
        print("Invalid choice. Defaulting to Easy.")
        return 10

limit = difficulty()

def guess_number(initial_attempt, ran_num):
    initial_attempt += 1
    start_time = time.time()
    
    guess = int(input(f"Enter a random number between 1 and {limit}: "))
    end_time = time.time()
    response_time = end_time - start_time
    print(f"It took you {response_time:.2f} seconds to respond.")
   
    if guess == ran_num:
        print(f"That is correct! It took you {initial_attempt} attempt(s) this round.")
        return initial_attempt, response_time
    elif guess > ran_num:
        print("Too high!")
        return guess_number(initial_attempt, ran_num) 
    else:
        print("Too low!")
        return guess_number(initial_attempt, ran_num)

def play_round(round_num, total_attempts, response_time):
    if round_num > num_user:
        average_attempts = total_attempts / num_user
        average_response_time = response_time / total_attempts
        print(f"\nGame over! You played {num_user} rounds.")
        print(f"Total attempts: {total_attempts}")
        print(f"Average attempts per round: {average_attempts:.2f}")
        print(f"Average response time: {average_response_time:.2f} seconds per attempt")
    else:
        print(f"\nRound {round_num}")
        
        ran_num = random.randint(1, limit)
       
        attempts, response_time = guess_number(0, ran_num)

        total_attempts += attempts
        response_time += response_time

        play_round(round_num + 1, total_attempts, response_time)

play_round(round_num, total_attempts, response_time)

#Periods 1-2 Aliyah Pargan 10-6-2024

print("Hi! Welcome to the Random Number Calculator!")
print("I will generate a random number between 1 and 100")

import random
num_random = random.randint(1,100)
user_number = int(input("Please enter a number: "))

print(" ")
print("Random number generated: " + str(num_random))
print("Please enter a number: " + str(user_number))

import math
Sum = num_random + user_number
Difference = num_random - user_number
Product = num_random * user_number
Quotient = num_random // user_number
Remainder = num_random % user_number
Square_root = (math.sqrt(num_random))
Power_random = (math.pow(user_number,num_random))

print(" ")
print("Results: ")
print("Your Number: " + str(user_number))
print("Sum: " + str(num_random), "+ " ,str(user_number) + " = " + str(Sum))
print("Difference: " + str(num_random), "-" ,str(user_number) + " = " + str(Difference))
print("Product: " + str(num_random), "*" ,str(user_number) + " = " + str(Product))
print("Quotient: " + str(num_random), "//" ,str(user_number) + " = " + str(Quotient))
print("Remainder: " + str(num_random), "%" ,str(user_number) + " = " + str(Remainder))
print("Square Root of Random Number: " + "sqrt(",str(num_random), ")" + " = " + str(Square_root))
print("Your Number to the Power of Random Number: " + str(user_number),"^", 
      str(num_random) + "=" + str(Power_random))



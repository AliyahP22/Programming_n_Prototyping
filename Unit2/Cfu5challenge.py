#09/30/2024 Periods 1-2 Aliyah Pargan

#little Canadian kid broke their piggy bank, you are to
#create a program to help them figure out how much
#money they have
# pennies = 1 cent
#nickles = 5 cents
#dimes = 10cents #quarters = 25c
#loonies = $1 or 100 cents 
#toonies = $2 or 200 cents 
#ask kid how much of each coin they have and calculate
#the total and give answer in decimals and in a combination

pennies = int(input("How many pennies do you have?"))
nickles = int(input("How many nickles do you have?"))
dimes = int(input("How many dimes do you have?"))
quarters = int(input("How many quarters do you have?"))
loonies = int(input("How many loonies do you have?"))
toonies = int(input("How many toonies do you have?"))

import math
total = float(pennies + nickles + dimes + quarters + loonies + toonies)
print("The amount of money you have is " + "$" + str(total))
print ("or " + "$" + str((loonies + toonies)) + " and " + str(quarters) + " quarters , " + str(dimes) + " dimes, " + str(nickles) + " nickles, " + str(pennies) + " pennies")

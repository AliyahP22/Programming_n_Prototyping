#10/1/2024 Periods 1-2 Aliyah Pargan

#little Canadian kid broke their piggy bank, you are to create a program to help them figure out how much money they have
# pennies = 1 cent nickles = 5 cents dimes = 10cents quarters = 25c loonies = $1 or 100 cents toonies = $2 or 200 cents 
#ask kid how much of each coin they have and calculate the total and give answer in decimals and in a combination

pennies = int(input("Enter an amount of pennies: "))
dimes = int(input("Enter an amount of dimes: "))
nickels = int(input("Enter an amount of nickels: "))
quarter = int(input("Enter an amount of quarters: "))
loonies = int(input("Enter an amount of loonies: "))
toonies = int(input("Enter an amount of toonies: "))

dimestopennies = dimes * 10
nickelstopennies = nickels * 5
quarterstopennies = quarters * 25
looniestopennies = loonies * 100
tooniestopennies = toonies * 200

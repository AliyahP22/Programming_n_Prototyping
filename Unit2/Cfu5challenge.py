#10/1/2024 Periods 1-2 Aliyah Pargan

#little Canadian kid broke their piggy bank, you are to create a program to help them figure out how much money they have
# pennies = 1 cent nickles = 5 cents dimes = 10cents quarters = 25c loonies = $1 or 100 cents toonies = $2 or 200 cents 
#ask kid how much of each coin they have and calculate the total and give answer in decimals and in a combination

#10-1-2024 Aliyah Pargan Periods 1-2
pennies = int(input("Enter an amount of pennies: "))
dimes = int(input("Enter an amount of dimes: "))
nickels = int(input("Enter an amount of nickels: "))
quarter = int(input("Enter an amount of quarters: "))
loonies = int(input("Enter an amount of loonies: "))
toonies = int(input("Enter an amount of toonies: "))

dimestopennies = dimes * 10
nickelstopennies = nickels * 5
quarterstopennies = quarter * 25
looniestopennies = loonies * 100
tooniestopennies = toonies * 200
total_pennies = dimestopennies + pennies + nickelstopennies + quarterstopennies+ looniestopennies + tooniestopennies
dollars = total_pennies // 100  
cents = total_pennies % 100  


print(f"You have a total of ${dollars}.{cents:02d}!")


remaining_cents = cents
num_quarters = int(remaining_cents // 25)
remaining_cents = int(remaining_cents % 25)
num_dimes = int(remaining_cents // 10)
remaining_cents = int(remaining_cents % 10)
num_nickels = int(remaining_cents // 5)
remaining_cents = int(remaining_cents % 5)
num_pennies = int(remaining_cents)

print(f"That's {dollars} dollars, {num_quarters} quarters, {num_dimes} dimes, {num_nickels} nickels, and {num_pennies} pennies.")




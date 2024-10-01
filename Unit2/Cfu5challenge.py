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
totalpennies = dimestopennies + pennies + nickelstopennies + quarterstopennies+ looniestopennies + tooniestopennies
total = totalpennies / 100


print("The total amount of money you have is $" + str(total))
print("Total value of coins: $" + "{:.2f}" .format(total_value))
 totalDollar = int(total_value // 1)
 print(totalDollar)
change = total_value - totalDollar
change_quarter = (change) % 4
inCents = int(change*100)
inQuart = int(change*4)
inDimes = int)change*10)-inQuart
inNickels = int(change*20)-(inDimes*2)
inCents = int(change*100)-(inNickels*10)
print(f"Your total is: ${totalDollars},{inQuarts}quarters, {inDimes}, dimes, {inNickels}nickles, {inCents}cents)


#Aliyah Pargan 
#Period 2
#1-7-2025
#CFU 18, which is a program that adds up all the prices in the following list

#version 1
prices = [1.95, 4.50, 0.99, 5.99]
total = 0 #initializing variabke

for price in prices:
    total += price
    
print("The Total Price is: ", total)


#version 2
prices = []
amount_prices = int(input("How many prices would you like to add? ")) #user input

#for loop to make code easier
for i in range(amount_prices):
    price = float(input("Enter price you would like to add: $"))
    prices.append(price)
    
total_price = sum(prices)
print("The total prices you added is: $ ",total_price)


#version 3
    

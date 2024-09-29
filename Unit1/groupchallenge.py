#Challenge 1
print("Perimeter of a rectangle")
length = int(input("Enter a number: "))
width = int(input("Enter a number: "))
perimeter = (2 * length) + (2 * width)
print("Perimeter of a " + str(length) + " by " +  str(width) + " rectangle is " + str(perimeter))

#Challenge 2 Aliyah Pargan
print("Fahrenheit to Celcius")
temp = float(input("Enter a fahrenheit temperature"))
celcius = (temp - 32) * 5/9
print(str(temp) + "is " + str(celcius) + "degrees")

#Challenge 3

print("The vertical velocity and time")
velocity = float(input("Enter a vertical velocity"))
time = float(input("Enter a time"))
import math
vertdist = (velocity * time) - (9.8 * time**2)
print("The vertical distance of this projectile object is " + str(vertdist))

#bonus
print("Distance between 2 points")
x1 = int(input("Enter a value for one point"))
y1 = int(input("Enter a value for one point"))
x2 = int(input("Enter a value for one point"))
y2 = int(input("Enter a value for one point"))
distance = ((x2 - x1)**2) + ((y2-y1)**2)**0.5

print("The distance between " + str(x2) + ", " + str(y2) + " is " + str(distance))

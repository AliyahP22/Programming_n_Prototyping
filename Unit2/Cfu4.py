#09-24-2024 Aliyah Pargan Periods 1-2. This CFU demonstrates the skills of using import math and how you can solve
#advanced math equations using python.
fname = input("What is your name ")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

import math
root1 = (-b + (b ** 2 - 4 * a * c) **0.5) /(2 * a)
root2 =  (-b - (b ** 2 - 4 * a * c) **0.5) /(2 * a)

print(fname + " the roots of your equation are " + "x = " + str(root1) , " and x = " + str(root2))


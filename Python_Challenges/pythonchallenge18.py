#Aliyah Pargan
#Period 1
#04-6-2025
#Python Coding Challenge 18, which would be to create a program using the function GCD to calculate
#the greatest common divisor between a and b

def gcd(a, b): #define function 
    #base case If b is 0, return a because the GCD of any number and 0 is the number itself.
    #return a because (a, 0) == a
    if b == 0:
        return a
    else: # Recursive case: If b is not 0, calculate the remainder of a divided by b.
        (a % b) #checks remainder
        return gcd(b, a%b)
    
    
print(gcd(48,18)) #expected output is 6
print(gcd(56,98)) #expected output is 14
print(gcd(101,10)) #expected output is 1
print(gcd(42,56)) #expected output is 14
print(gcd(17,13)) #expected output is 1

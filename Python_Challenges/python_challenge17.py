#Aliyah Pargan
#Period 1-2
#04-3-2025
#Python Coding Challenge 17, which is a program created with functions and if statements to determine
#if a is a power of b

def is_power(a,b): #define function with 2 parameters
    # Base case: if a is smaller than b, it cannot be a power of b.
    if a < b: #checks if a is less than b
        return False
  
    
    # Base case: if a equals b, return True because a is b^1.
    if a == b:
        return True
    
    #check to see if a is divisible by b
    if a % b == 0: #checks to see if there is a remainder (modulos) 
        return is_power(a//b, b) #calls function over again
    else:
        return False
    
    
print(is_power(16,2)) #expected output is true
print(is_power(27,3))#expected output is true
print(is_power(9,2))#expected output is false
print(is_power(81,3))#expected output is true
print(is_power(32,5))#expected output is false

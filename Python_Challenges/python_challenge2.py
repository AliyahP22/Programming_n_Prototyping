#Aliyah Pargan
#Periods 1-2
#02-27-2025
#Python Coding challenge 2, which tests our python skills using functions and len.


def right_justify(s): #define function and parameters
    leading_space = 70 - len(s) #calculates the amount of spaces 
    print(' ' *leading_space +s) #' ' gives space and prints the string with leading space
    
    
    
right_justify("allen") #call function

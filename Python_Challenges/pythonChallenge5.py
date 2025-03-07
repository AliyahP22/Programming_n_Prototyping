#Aliyah Pargan
#Period 1-2
#03-6-2025
#Python Challenge 5, which tests our knowledge of using functions and conditional
#statements(if statements, elif statements, and if else statements
#a**n + b**n = c**n  for any values of n greater than 2 is Fermats Last Theorem


def check_fermat(a, b,c,n): #define function with 4 parameters
    if n > 2:#checks to see if the condition n > 2 is true and would execute the next line of code
        if (a**n) + (b**n) == (c**n): #checks to see if formula works
            print("Holy Smokes! Fermat was wrong!!")
        else:#alternate option if condition is proven false
            print("No, that doesn't work")
            
check_fermat(3,4,2,5) #call function with testing values 
check_fermat(2,4,6,8)#call function with testing values
check_fermat(3,5,9,3)#call function with testing values

#Aliyah Pargan
#period 1
#03-10-2025
#Python coding challenge 6, which asks us to create a function that tests if the values inputted can form a triangle
#then asks us to modify our code to ask the users to use user input to input the side lengths 

#prompt 1: 
def _triangle(a,b,c): #define function with 3 parameters
    if (a+b) == c: #checks to see if 2 sides added together is equal to the value of third side
        print("Yes, forms a degenerate triangle")
    elif a > (b+c) or b > (a+c) or c > (a+b): #checks to see if any value is greater than the sum of an individual value
        print("No that doesn't work")
    else:
        print("Yes") #alternate output if both conditions executed are false
        
_triangle(2,1,6) #call function with testing value
_triangle(3,3,3) #call function with testing value
_triangle(2,1,3) #call function with testing value


#modifications(prompt 2):
def __triangle(): #define new function
    a = int(input("Enter first stick length")) #prompts user to input an integer
    b = int(input("Enter second stick length")) #prompts user to input an integer
    c = int(input("Enter third stick length")) #prompts user to input an integer
    
    _triangle(a,b,c) #call old function so it can calculate the side lengths 



__triangle() #call function

#Aliyah Pargan
#Periods 1-2
#03-5-2025
#Python Coding Challenge #4, which tests our ability to create and define functions that could
#result in an image, like a grid


#original grid
def drawGrid(): #define function
    for row in range(2): #makes a loop that repeats 2 times 
        print("+", "-", "-", "-", "-", "+", "-", "-", "-", "+", sep='', end=' ') #creates the top part
        print() 
        for space in range(4):  
            print("|", " " * 1, "|", " " * 1, "|", " " * 1) #creates the spaces in the rows
            print() #prints in a separate line 

    
    print("+", "-", "-", "-", "-", "+", "-", "-", "-", "+", sep='', end=' ') #creates the bottom rows
    print()#prints in a separate line 
        
drawGrid() #call function


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

#grid with 4 rows and 4 columns
def draw_grid(): #call function
    for row in range(4): #creates for loop that runs exactly 4 times  
        print("+", "-", "-", "-", "-", "+", "-", "-", "-", "+","+", "-", "-", "-", "-", "+","+", "-", "-", "-", "-", "+", sep='', end=' ')
        print() #prints in a separate line  
        for space in range(4): #loop runs exactly 4 times
            print("|", " " * 4, "|", " " * 4, "|", " " * 4, "|", " " * 4, "|", sep='', end=' ') #creates spaces within the rows
            print() #prints in a separate line 


    print("+", "-", "-", "-", "-", "+", "-", "-", "-", "+","+", "-", "-", "-", "-", "+","+", "-", "-", "-", "-", "+", sep='', end=' ')
    print() #prints in a separate line


draw_grid() #call function




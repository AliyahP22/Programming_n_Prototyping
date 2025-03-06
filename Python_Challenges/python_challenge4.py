#Aliyah Pargan
#Periods 1-2
#03-5-2025
#Python Coding Challenge #4, which tests our ability to create and define functions that could
#result in an image, like a grid


#original grid
def drawGrid():
    for row in range(2):  # 4 rows
        print("+", "-", "-", "-", "-", "+", "-", "-", "-", "+", sep='', end=' ')
        print() 
        for space in range(4):  
            print("|", " " * 1, "|", " " * 1, "|", " " * 1)
            print()  

    
    print("+", "-", "-", "-", "-", "+", "-", "-", "-", "+", sep='', end=' ')
    print()  
        
drawGrid()


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

#grid with 4 rows and 4 columns
def draw_grid():
    for row in range(4):  
        print("+", "-", "-", "-", "-", "+", "-", "-", "-", "+","+", "-", "-", "-", "-", "+","+", "-", "-", "-", "-", "+", sep='', end=' ')
        print()  
        for space in range(4): 
            print("|", " " * 4, "|", " " * 4, "|", " " * 4, "|", " " * 4, "|", sep='', end=' ')
            print()  


    print("+", "-", "-", "-", "-", "+", "-", "-", "-", "+","+", "-", "-", "-", "-", "+","+", "-", "-", "-", "-", "+", sep='', end=' ')
    print() 


draw_grid()




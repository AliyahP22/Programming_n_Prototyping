#Aliyah Pargan
#Periods 1-2
#03-5-2025
#Python Coding Challenge #4, which tests our ability to create and define functions that could
#result in an image, like a grid


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

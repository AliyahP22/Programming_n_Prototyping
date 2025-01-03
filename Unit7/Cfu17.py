#Aliyah Pargan
#Periods 1-2
#01-3-2025
#CFU 17, which is a review of code learnt in class and build in formatting functions

box = "MerlinPen"
def formating(box):
    userInput = int(input("Choose: 1, 2, 3, 4, 5, 6"))
    if userInput == 1:
        #Captalize the first letter of the variable
        box = box.capitalize()
        print(box)
    elif userInput == 2:
        #find and return the position of a value in the string
        box = box.find("e")
        print(box)
    elif userInput == 3:
        #return true if the variable is a number
        box = box.isdigit()
        print(box)
    elif userInput == 4:
        #output the variable all lowercase
        box = box.lower()
        print(box)
    elif userInput == 5:
        #replace an index value item for another
        print(box.replace("n", "a"))
    elif userInput == 6:
        #output the variable all lowercase
        box = box.upper()
        print(box)
    else:
        print("Not a valid option")
formating(box)



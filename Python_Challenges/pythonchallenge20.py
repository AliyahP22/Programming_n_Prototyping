#Aliyah Pargan
#Period 1
#04-8-2025
#Python Coding challenge 20

def avoids(word, forbiddenLetters): #define function with both parameters
    for letter in forbiddenLetters: #runs loop for each word in list
        if letter in word:
            return True
        return False #returns false if condition executed is false
    
    
def main_part(): #main function 
    forbiddenLetters = input("Enter a string of forbidden letters!") #user inputs a letter
    forbiddenLetters = input("Enter a string of forbidden letters!")
    forbiddenLetters = input("Enter a string of forbidden letters!")
    forbiddenLetters = input("Enter a string of forbidden letters!")
    forbiddenLetters = input("Enter a string of forbidden letters!")
    words_list = ["colors", "dog", "cat", "bird", "apple", "dress", "love", "grapes", "pretty",
                  "hamster", "coding", "python", "computer", "radio" "banana", "papaya"]
    count = 0 #initializer
    for word in words_list:
        if avoids(word, forbiddenLetters):
            count+=1 #increases count
    print(f"Total words without forbidden letters: {count}")
            

main_part() #call function   

#Aliyah Pargan
#Period 1
#04-10-2025
#Python Coding challenge 22


#list for challenge
word_list = ["education", "dog", "cat", "puppy", "butterfiles", "coding", "song", "fly", "laptop", "music", "rhythm"]
def uses_all(word, required_letters):
    for letter in required_letters: #loops through each word 
        if letter not in word:
            return False
        return True #returns true if condition executed is false
    
     
print(uses_all("puppy", "aeiou")) #call function
print(uses_all("coding", "coigd"))#call function
print(uses_all("pretty", "aeiou"))#call function
print(uses_all("butterflies", "biuer"))#call function


#challenge
def count_words(word_list, required_letters):
    count = 0 #initializer
    for word in word_list:
        if uses_all(word.lower(),required_letters): #checks if lowercase letters has required letters
            count+=1 #increase count by increments of 1
            return count
        
vowelCount = count_words(word_list, "aeiou")
print(f"Words with all the vowels: {vowelCount}")

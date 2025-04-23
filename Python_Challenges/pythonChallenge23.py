#Aliyah Pargan
#Period 1
#04-22-2025
#Python Coding Challenge 23, which is a program that checks to see if the letters
#in a word appear in alphabetical order


def _abecedarian(word): #define function with string as parameter 
    return list(word) == sorted(word)


#word list that would be used to test the function
words_list = ["abcdef", "noon", "abc", "art", "ace", "car", "abe", "hi", "jade", "aegilops", "dance"]

for word in words_list: #loop to check each word, print the word, and see if its an abecedarian word
    print(f"{word}: {_abecedarian(word)}") #prints word and checks
    
word_count = 0 #initializer
for word in words_list:
    if _abecedarian(word): #call function to check
        word_count+= 1 #increase count by increments of 1
        
        
print("Total Abecedarian Words: ", word_count)

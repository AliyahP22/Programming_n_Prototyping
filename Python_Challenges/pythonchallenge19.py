#Aliyah Pargan
#Period 1
#04-7-2025
#Python Coding challenge 19, which takes a list of words and filters it based on
#which words contain e and which dont. Then returns the percentage of words that do not
#contain e

def no_e(word):
    for letter in word:#repeats loop for each word
        if letter.lower() == "e": #checks if the word has an e
            return False 
    return True #returns true only if condition is proven false     
def filter_words_without_e(words_used):
    words_no_e = [word for word in words_used if no_e(word)] #creates a list for words with no e
    
    total = len(words_used) #counts total length of words(Total words_    
    words_no_e_total = len(words_no_e)
    
    if total == 0:
        percent = 0  #sets percent to 0 if total words are 0
    else:
        percent = (words_no_e_total / total) * 100 #formula for percentage
    
    print("Words that don't contain e:", words_no_e)
    print(f"Percentage: {percent:.2f}%") #rounds to 2 decimal points


words_used_sample = ["apple", "dog", "flowers", "name", "consists", "words", "black", "cat", "birds", "phone", "bag"]
filter_words_without_e(words_used_sample) #call function with sample list 

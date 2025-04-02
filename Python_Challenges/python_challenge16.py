#Aliyah Pargan
#04-2-2025
#Period 1
#Python coding challenge 16, which is a series of functions to check if a word is a palindrome

def first_letter(word): #function to return first letter of string
    if word: #checks to see if string is empty
        return word[0]#returns letter in index 0 (First index)
    else:
        return None 
    
def last_letter(word):#function to return last letter of string
    if word:#checks if string is empty
        return word[-1] #returns letter in last index
    else:
        return None
    
def middle(word):
    if len(word)> 2 : #focuses on middle length of string
        return word[1:-1]# returns first and last letters
    else:
        return ''
    
def _palindrome(word): #function to check if word is palindrome
    #palindrome is word that has one letter or if the word is empty
    if len(word) <=1: #if it has one or less letters, it is a palindrome
        return True
        
    if first_letter(word) == last_letter(word):#if the first letter = last letter, recursively checks middle part
        return _palindrome(middle(word))#word would be considered a palindrome
    else:
        return False  
              
print(_palindrome("noon")) #output should be "True"
print(_palindrome("redivider"))#output should be "True"
print(_palindrome("hello")) #Output should be "false"
print(_palindrome("a"))#output should be "True"
print(_palindrome(""))#output should be "True"

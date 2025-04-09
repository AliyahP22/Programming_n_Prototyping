#Aliyah Pargan
#04-9-2025
#Period 1
#Python Coding challenge 21 which would sort through the words and see if it has 
#allowed letters or not and based on the results, return true or false



def uses_only(word, allowed_letter): #define function
    for letter in word:
        if letter not in allowed_letter: #if no allowed letters, output is false
            return False
        return True
    
    
    
#TEST FUNCTION    
print(uses_only("hello",  "a,b,c,d,f,g"))
print(uses_only("cat" , "a,b,c,d,e,f"))
print(uses_only("python" , "a,b,e,i,u,p"))
print(uses_only("code", "a,b,d,f,g,i"))
        
#CHALLENGE EXECUTION Create a sentence using only the letters a, c, e, f, h, l, o.

print(uses_only("Hello call chef with cello", "a, c, e, f, h, l, o"))
print(uses_only("hello call chef cello", "a, c, e, f, h, l, o"))
print("Sentence formed: Hello call chef cello")

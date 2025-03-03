#Aliyah Pargan
#period 1
#03-3-2025
#Python coding challenge, which tests our knowledge of parameters and defining and calling functions


#original
def do_twice(f): #define function
    f() #function is a parameter 
    f()
    
def print_spam():
    print ("spam")#value to be printed
do_twice(print_spam)#call function

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") #separates original from modifications
#modifications
def do_twice(f,v): #places a function and value in its parameters
    f(v)
    f(v)
    
def print_twice(s):
    print(s)
    print(s)#prints the string
    
do_twice(print_twice, "spam") #call function, spam is the string to be printed 

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") #serves to separate function do_twice from function do_four
    

def do_four(f,v):#define new function
    do_twice(f,v)
    do_twice(f,v)
    
do_four(print_twice,"spam") #call function

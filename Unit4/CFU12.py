#Periods 1-2 Aliyah Pargan 10-29-2024
#CFU 12, which has a set password, allows users to keep guessing
#until they get the right password. This program uses while loops


def version_1():
    password = "simonsync"
    user_guess = input("What is the password")
    while password != user_guess:
        print("Wrong, please try again")
        user_guess = input("What is the password?")
    
    print("Correct, you may enter!!")

def version_2():
    password = "simonsync"
    guess = 3
    attempts = 0
    
    while guess < 3:
        user_guess = input("What is the password?")
        if user_guess != password :
             print("Wrong, please try again")
             guess-=1
             attempts+=1
        elif user_guess!= password and guess == 0:
            print("Out of attempts, try again!")
             
        else:
            print("Correct, you may enter!!")
            

version_1()            
version_2()



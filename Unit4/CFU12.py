#Periods 1-2 Aliyah Pargan 10-29-2024
#CFU 12, which has a set password, allows users to keep guessing
#until they get the right password. This program uses while loops


def version_1():
    password = "simonsync"
    user_guess = " "
    while password != user_guess:
        print("Wrong, please try again")
        user_guess = input("What is the password?")
    
    print("Correct, you may enter!!")


def version_2():
    password = "simonsync"
    num_tries = 0
    while num_tries < 3:
        user_guess = input("What is the password?")
        if user_guess != password:
             print("Wrong, please try again")
             num_tries+=1
         
        else:
            print("Correct, you may enter!!")
            num_tries+=1
            return user_guess
        print("Max Attempts: 3")
        print(f"Your Attempts: {num_tries}")
        if num_tries == 3:
            print("Out of attempts, try again!")
        else:
            print(" ")
            

version_1()            
version_2()


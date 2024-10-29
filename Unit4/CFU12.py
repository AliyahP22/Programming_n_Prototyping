#Periods 1-2 Aliyah Pargan 10-29-2024
#CFU 12, which has a set password, allows users to keep guessing
#until they get the right password. This program uses while loops

password = "simonsync"
user_guess = " "
num_tries = 3

while password != user_guess:
    while num_tries < 3:
        print("Wrong, please try again")
        user_guess = input("What is the password?")
        if num_tries == 0:
            print("Out of tries, Sorry!")

    
print("Correct, you may enter!!")



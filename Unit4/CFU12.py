#Periods 1-2 Aliyah Pargan 10-29-2024
#CFU 12, which has a set password, allows users to keep guessing
#until they get the right password. This program uses while loops

#Version 1
password = "simonsync"
user_guess = " "

while password != user_guess:
    print("Wrong, please try again")
    user_guess = input("What is the password?")

    
print("Correct, you may enter!!")

#period 1-2 Aliyah Pargan 10-28-2024
#CFU 11, which is an introduction to loops and range. the first task is a loop that prints a number sequence
#10-70. Option 2 is a decimal number sequence. Option 3 is the 99 bottles of beer on the wall song. Using 
#functions, the user can pick what option they want. 

def print_numbers_10_to_70():
    for num in range(10, 71, 10):
        print(num) #option 1
       

def print_numbers_0_to_10():
    num = 0
    while num <= 10:
        print(num)
        num += 0.5 #option 2

def sing_99_bottles():
    num_bottles = 99
    while num_bottles > 0:
        print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
        num_bottles -= 1
        print(f"Take one down, pass it around, {num_bottles} bottles of beer on the wall.\n")
    print("No more bottles of beer on the wall.") #option 3

def main():
    user_choice = input("Which option would you like! Please choose from 1-3!")
    if user_choice == '1':
        print_numbers_10_to_70()
    elif user_choice == '2':
        print_numbers_0_to_10()
    elif user_choice == '3':
        sing_99_bottles()
    else:
        print("Please enter a number.")

# Run the main program
main()

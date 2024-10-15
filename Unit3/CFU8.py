#periods 1-2 Aliyah Pargan 10-15-2024
#CFU8, which is a mini review about python functions, conditionals, if statements and else if statements

user_question = input("Did you order delivery?")
if user_question == "yes":
    print("Great!")
else: 
    print("NO?! So who is cooking?")
    

cost = int(input("How much did the food cost?"))
people = int(input("How many people are splitting the order?"))
cost_split = cost // people

if user_question == "yes":
    print("How much did the food cost?")
    print("The cost per person is " + "$" + str(cost_split))
else: 
    print("NO?! So who is cooking?")

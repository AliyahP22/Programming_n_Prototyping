groceries = ["Eggs", "Apples", "Milk", "Bread"]

names = ["David", "Aliyah", "Rohaan", "Betsy", "Nabila", "Brithany", "Micah", "Tasfia", "Michael", "Armina", "Nataly", "Towaf", "Vashti", "Syeda", "Devesh", "Rafael", "Jannatul"]
 
ages = [17.2, 16.11, 16.6, 16.2, 16.5, 18, 16.4, 16.2, 16.3, 16.11, 16.11, 16.6, 17.4, 16.5, 16.11, 17.2, 16.2]   
print(groceries[0])

print(names[0] + " is " + str(ages[0]) + " years old")
print(groceries[0:3])

print(str(names[1:5]) + " is " + str(ages[1:5]) + " years old")

for i in range(len(ages)):
    print("My friend " + names[i] + " is " + str(ages[i]) + " years old")

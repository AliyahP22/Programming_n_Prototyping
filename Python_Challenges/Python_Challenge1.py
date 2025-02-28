import math #used for formulas 
def sphere_volume(radius): #define function
    volume = (4/3)* math.pi * (radius ** 3) #applying the formula of the volume of a sphere 
    return volume 
radius = 5 #initializing radius value 
result = sphere_volume(radius) #the result has the value of the function itself
print(f"1. The volume of the sphere with the radius of 5 is {result:.2f}") #Makes sure answer is rounded to 2 decimal points


def wholesale_cost (copies): #define function
    cover_price = 24.95 #initializes cover price in variable
    discount= 0.40 #initializes discount in variable
    first_copy = 3 #initializes first copy price in variable
    ship_after = 0.75#initializes shipping price after in variable 
    discount_price = cover_price * (1-discount) #calculates discount price
    total_book = discount_price * copies #calculates total book costs
    shippingcost = first_copy + (ship_after * (copies - 1)) #calculates total shipping costs
    total = total_book + shippingcost 
    print(f"2. The total is ${total:.2f}") 
wholesale_cost(60) #call function



def running_time (start_hour, start_minutes): #define function and parameters
    easy_pace = 8*60+15 #turning 8 mins into secs and adding 15 secs
    tempo_pace = 7*60+12 #trunign 7 mins into secs and adding 12 secs
    total_time_sec= easy_pace*2 + (tempo_pace*3) #calculate total time
    total_min = total_time_sec // 60 #calculate total minutes
    total_secs = total_time_sec % 60 #the remainder which will be the seconds
    end_mins = total_min + start_minutes #get ending minutes by addition
    end_hour = start_hour #storing the start hour with the end hour
    if end_mins >= 60: #if end mins is greater or equals to 60 it will add another hour in it
        end_hour += end_mins // 60 #this shows how the minuteswill add another hour after it turns 60 mins
        end_mins = end_mins % 60 #this is for adding a minute every 60 secs
        return end_hour, end_mins 
end_hour, end_mins = running_time(6,52) 
print (f"3. You arrive home for breakfast at {end_hour}:{end_mins} AM") #creating a sentence using formating and making it look like actual time



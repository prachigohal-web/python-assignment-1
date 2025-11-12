"""
project:Daily Calorie Tracker(CLI)y
Name-Prachi Gohal
Date-30 october 2025

Description: A simple python programme to record meals,track daily calorie intake and help compare our callories
"""
#-----------------#
           #TASK-1#
#-----------------#
print("=================================")       
print("Welcome to calorie tracker")    
print("=================================\n")
#Function of this code#
print("Tracks your daily calorie intaker")
print("you can know your total and average calorie intake")
print("We can use this code to meet our daily calorie intake goal \n")
#------------------#
          #TASK-2#
      #INPUT AND DATA COLLECTING#
#------------------#
meal_names=[]
calorie_values=[]
 conf=input("would you like to add meals?(yes/no):").lower()

if conf=="yes":
    meal_count=int(input("how many meals do you want to enter today?")) 
    for i in range(meal_count):
        print("\n meal",i+1)   
        meal=input("enter meal name:") 
        calories=int(input("enter calories for this meal:"))
        meal_names.append(meal)   
        calorie_values.append(calories) 
        print("\nYour meals and calories are saved")
else:
    print("\nOkay! remember to add your meals later.")      
#-------------------#
             #TASK-3 & 4#
         #CALLORIE CALCULATION AND WARNING#    
#-------------------# 
total_calories=sum(calories_values)     
average_calories=total_calories/len(calorie_values)     
daily_limit=int(input("\nEnter your daily calorie limit:"))   
print("\n----Calorie Summary----") 
print("Total Calories:",total_calories) 
print("Average per meal:",average_calories)   
if total_calories<=daily_limit:
    print("you are within your total calorie limit")
else:
    print("you have exceeded your daily calorie limit")    
#------------------#
           #TASK-5#
      #PRINTING A FORMATTED OUTPUT#
#-----------------#
print("\nCalorie Report")             
print("-------------")  
for i in range(len(meal_names)):
    print(meal_names[i],"=",calorie_values[i],"calories")
    print("-------------")
    print("total calories:",total_calories)
    print("average calories:",average_calories)


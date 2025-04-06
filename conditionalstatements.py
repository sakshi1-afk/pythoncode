    #CONDITIONAL STATEMENTS
# Conditional statements are used to perform different actions based on different conditions.
# Python supports the following conditional statements:
     # 1. if statement
age = 24

if(age >= 18 ):
    print("can vote & apply for driving license")
 #this code checks if the age is greater than or equal to 18. If true, it prints that the person can vote and apply for a driving license.
    print("can drive")

    # 2. if-else (elif)statement
# The elif statement is used to check multiple conditions. It stands for "else if".
# The elif statement allows you to check multiple conditions in a single if statement.

    light = "pink" #we can change the value of light to "yellow" or "green" to test different conditions

    if (light == "red"):
        print("stop")
    elif (light == "yellow"):
        print ("wait")
    elif (light == "green"):
        print("go")

        #3.else statement
    # The else statement is used when the condition is false.
    # It is an optional statement that can be used with the if statement.
    # The else statement is executed when the if condition is false.

    else:
        print("light is broken")

    age = 12

    if (age >= 18):
        print("can vote and drive")

    else:
        print("cannot vote and take driving test")
     #indentation is important in Python. The code inside the if and else blocks must be indented properly.

     
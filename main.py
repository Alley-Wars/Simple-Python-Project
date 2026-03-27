#Menu Hub
print("Welcome to Brandon's Simple Projects!")
print("Please select one of the project below. (Numbers only or else!)")
print("1. Simple Calculator\n2. Random Number Game\n3. Word Cruncher\n")
#Import from other python file
try:
    answer = int(input())
    if answer == 1:
        from simple_cal import *
    elif answer == 2:
        from random_num import *
    elif answer == 3:
        from word import *
except ValueError:
    print("ERROR NUMBERS ONLY OR ELSE!!")

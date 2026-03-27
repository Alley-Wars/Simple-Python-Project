#Calculator 
import math
print("Welcome to 'THE MASTER' Calculator!")
def cal_master():
    try:
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
        ans = (int(input("Choose Function:\n (+) 1\n (-) 2\n (*) 3\n (/) 4\n")))
        if ans == 1:
            return num1 + num2
        elif ans == 2:
            return num1 - num2
        elif ans == 3:
            return num1 * num2
        elif ans == 4:
            return num1 / num2 if num2 != 0 else "Cannot Divide by Zero!"
    except ValueError:
        return "Error Numbers ONLY!!"

    
print(cal_master())

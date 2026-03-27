import random

random_num = random.randint(1, 10)
attempt = 3

while attempt > 0:
    try:
        guess_num = int(input(f"Hello pick a number you only have {attempt} chances! "))
        
        if guess_num == random_num:
            print("You got it!")
            break
        else:
            print("Next time buddy")
            attempt -= 1

    except ValueError:
        print("Error numbers only!")

if attempt > 0:
    print("YOU WON!!")

if attempt == 0:
    print(f"GAME OVER! The number was {random_num}")

import random

random_num = random.randint(1, 11)
count = 0
attempt = 4
while count < 3:
    count += 1
    for n in range(random_num):
        try:
            if attempt == 1:
                print("Well times up!")
                break
            
            attempt = max(0, attempt - 1)
            guess_num = int(input(f"Hello pick a number you only have {attempt} chances! "))
            
            if guess_num == random_num:
                print("You got it!")
                break
            else:
                print("Next time buddy")
    
        except ValueError:
            print("Error numbers only!")

import random

PC_guess_number = random.randint(1, 100)

Guess_number = 0
while True:
    My_guess_number = int(input("Guess my number: "))
    Guess_number = Guess_number + 1
    if PC_guess_number == My_guess_number:
        print("Congratulations, you guessed it in {} attempts!" .format(Guess_number))
        break
    elif PC_guess_number > My_guess_number:
        print("try bigger number")
    else:
        print("try smaller number")

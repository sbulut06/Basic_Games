  
import random
smallest_number = 1
biggest_number = 100
attempt = 0
while True:

    print(smallest_number, "-", biggest_number)

    PC_guess_number = random.randint(smallest_number, biggest_number)

    Answer = input(str(PC_guess_number) +" is your guess? [y]es / [b]igger / [s]maller :")

    attempt += 1


    if Answer == "y":
        print("Guessed! in a {} attempts" .format(attempt))
        break
    elif Answer == "b":
        print("I have to try bigger")
        smallest_number = PC_guess_number + 1
    else:
        print("I have to try smaller")
        biggest_number = PC_guess_number - 1

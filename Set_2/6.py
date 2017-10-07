import random

print("It's a Game about your\nprediction power!")

rand = random.randrange(10)

inp = int(input("Enter your guess: "))

while rand != inp:
    print("Failed! generated number is: ", rand)
    rand = random.randrange(10)
    inp = int(input("Enter your guess again: "))

else:
    print("Well guessed!", rand)
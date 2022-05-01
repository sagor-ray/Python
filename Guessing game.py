import random

while 1:
    n = int(input("Enter your guess number between 1 to 5: "))
    randomNumber = random.randint(1, 5)
    if randomNumber == n:
        print("Congratulation, You are the Winner!!!!!")
        break
    else:
        text = "Oops, The number was {}.Try again!!!!"
        print(text.format(randomNumber))


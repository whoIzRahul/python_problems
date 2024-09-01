import random
randomNumber = random.randint(1, 10)
print("I have chosen a number between 1 and 10. Try to guess it.")
while True:
    guess = int(input("Your guess: "))
    if guess == randomNumber:
        print("Correct")
        break
    elif guess < randomNumber:
        print("Too low")
    else:
        print("Too high")
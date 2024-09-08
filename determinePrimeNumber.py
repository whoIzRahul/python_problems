# input from the user
number = int(input("Enter a number: "))
# number of dividers
dividers = 0

for i in range(1, number + 1):
    if number % i == 0:
        dividers += 1

if dividers == 2:
    print("The number is prime.")
else:
    print("The number is not prime.")

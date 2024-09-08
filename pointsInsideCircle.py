import random


# N = total number of points inside the square
def calculateApproximateOfPi(N):
    n = 0  # number of points inside the circle
    loopCounter = N
    while loopCounter > 0:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        #  (x, y)
        # checking if this point falls inside the circle using the formula x^2 + y^2 <= 1
        if x**2 + y**2 < 1:
            n += 1
        loopCounter -= 1
    print(n, N)
    print("Approximate value of pi: ", 4 * n / N)


pointsInsideSquare = int(input("Enter the number of points inside the square: "))

calculateApproximateOfPi(pointsInsideSquare)

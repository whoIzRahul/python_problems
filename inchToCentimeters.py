while True:
    n = int(input("Enter the length in inches: "))
    if n < 0:
        break
    print(n, "inches in centimeters is", n * 2.54, "cm")

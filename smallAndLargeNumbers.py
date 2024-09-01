smallest = None
largest = None
print("Enter a blank line to finish.")
while True:
    n = input("Enter a number: ")
    if n == "":
        print("The smallest number is:", smallest)
        print("The largest number is:", largest)
        break
    if smallest == None or float(n) <= smallest:
        smallest = float(n)
    if largest == None or float(n) >= largest:
        largest = float(n)
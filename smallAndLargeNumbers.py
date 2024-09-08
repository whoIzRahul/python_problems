smallest = None
largest = None
print("Enter a blank line to finish.")
number = input('enter a number')
while True:
    n = input("Enter a number: ")
    if n == "":
        print("The smallest number is:" + smallest)
        print("The largest number is:" + str(largest))
        break
    if smallest == None or float(n) <= smallest:
        smallest = float(n)
    if largest == None or float(n) >= largest:
        largest = float(n)

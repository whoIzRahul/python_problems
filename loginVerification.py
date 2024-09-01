username = "python"
password = "rules"
limit = 5
while limit > 0:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")
    if username_input == username and password_input == password:
        print("Welcome!")
        break
    else:
        print("Invalid username or password. Try again.")
        limit -= 1
        if limit == 0:
            print("You have reached the maximum number of attempts. Try again later.")
            break
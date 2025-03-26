#Yes No
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            print("You selected Yes")
        elif response == "no" or response == "n":
            print("You selected No")
        else:
            print("That value is invalid. Please enter 'yes' or 'no'")
while True:
    check = yes_no("Do you like coffee? ")
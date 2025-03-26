response = ''
def number_checker(question):
    global response
    error = "Please enter a measurement greater than 0"

    while True:
        response = input(question).lower()

        try:
            response = float(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

while True:
    test_int = number_checker("Enter a measurement greater than 0:\n")
    if test_int != '':
        print(f"You entered {test_int}")



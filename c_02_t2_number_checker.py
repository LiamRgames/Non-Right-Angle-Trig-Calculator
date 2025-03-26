response = ''
def number_checker(question):
    global response

    while True:
        response = input(question).lower()
        error = "ERROR | Please enter a measurement between 5 and 10"

        try:
            response = float(response)

            if 5 < response < 10:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

while True:
    test_int = number_checker("Enter a measurement between 5 and 10:\n")
    if test_int != '':
        print(f"You entered {test_int}")



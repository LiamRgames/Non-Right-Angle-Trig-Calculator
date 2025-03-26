response = ''
HIGH = 10
LOW = 5
def number_checker(question):
    global response

    while True:
        response = input(question).lower()
        error = f"Please enter a measurement between {LOW} and {HIGH}"

        try:
            response = float(response)

            if LOW > response:
                error = "That number is too low"
                print(error)
            elif response > HIGH:
                error = "That number is too high"
                print(error)
            else:
                return response

        except ValueError:
            print(error)

while True:
    test_int = number_checker(f"Enter a measurement between {LOW} and {HIGH}:\n")
    if test_int != '':
        print(f"You entered {test_int}")



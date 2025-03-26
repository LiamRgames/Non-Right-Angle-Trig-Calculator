def not_blank(question):
    numbers_in_response = 0
    while True:
        response = input(question)
        if response != '':
            for char in response:
                if char.isdigit():
                    numbers_in_response += 1
            if numbers_in_response == 0:
                return response
            else:
                print("There was a number in your response. Please try again")
                numbers_in_response = 0
        else:
            print("That value is invalid")


while True:
    who = not_blank("Please Enter Your Name:\n")
    print(f"Hello {who} :)")
response = ''
def string_checker(question, answers, len_letters):
    while True:
        global response
        response = input(question).lower()
        for i in answers:
            if response == i:
                response = i
                return response
            elif response == i[:len_letters]:
                response = i
                return response

        print(f"That response is invalid, please select an option from the following:\n{answers}")

yesno = ["yes","no"]
money = ["cash", "credit"]
check = string_checker("Do you like coffee(yes or no)?\n", yesno, 1)
print(f"You chose {response}")
funds = string_checker("Would you like to pay with Cash or Credit?\n", money, 2)
print(f"You chose {response}")
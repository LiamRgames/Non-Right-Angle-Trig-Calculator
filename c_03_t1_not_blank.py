def not_blank(question):
    while True:
        response = input(question)
        if response != '':
            return response
        else:
            print("That value is invalid")


while True:
    who = not_blank("Please Enter Your Name:\n")
    print(f"Hello {who} :)")
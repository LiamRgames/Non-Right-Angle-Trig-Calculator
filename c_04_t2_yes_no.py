response = ''
def string_checker(question, answers):
    while True:
        global response
        response = input(question).lower()
        for i in answers:
            if response == i:
                response = i
                return response
            elif response == i[0]:
                response = i
                return response

        print(f"That response is invalid, please select an option from the following:\n{answers}")

colours = ["blue", "red", "green", "yellow"]
difficulty = ["easy", "medium", "hard"]
better = ["python", "java"]
check = string_checker("What are my favourite colours(full word or first letter only)?\n", colours)
print(f"You chose {response}")
level = string_checker("What difficulty do you want(Easy, Medium or Hard?): ", difficulty)
print(f"You chose {response}")
programming_lang = string_checker("What Programming Language do you like most(Python or Java)? ", better)
print(f"You chose {response}")
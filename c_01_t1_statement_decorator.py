def statement_decorator(statement, decoration):
    global user_decoration
    global user_statement
    print(f"{3*user_decoration} {user_statement} {3*user_decoration}")

while True:
    user_statement = input("Enter a statement to be decorated:\n")
    if user_statement != '':
        user_decoration = input("Enter 1 character to decorate this message, maybe an emoji?\n")
        if len(user_decoration) == 1:
            statement_decorator(user_statement, user_decoration)
        else:
            user_statement = ''
            user_decoration = ''
    else:
        user_statement = ''
        user_decoration = ''

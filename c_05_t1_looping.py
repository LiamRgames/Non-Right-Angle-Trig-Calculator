#Definitions
import math
a = ''
b = ''
c = ''
A = ''
B = ''
C = ''
response = ''

options = ["angle","side length","area"]

#Functions
def statement_decorator(message, decoration, lines):
    if lines == 1:
        print(f"{decoration*3} {message} {decoration*3}")
    elif lines == 2:
        print(f"{decoration * 3} {message} {decoration * 3}")
        for char in range(0, len(message) + 8):
            print(decoration, end="")
        print()
    else:
        for char in range(0, len(message) + 8):
            print(decoration, end="")
        print(f"\n{decoration*3} {message} {decoration*3}")
        for char in range(0, len(message) + 8):
            print(decoration, end="")
        print()
def instructions():
    statement_decorator("Instructions", "=", 1)
    print('''

Welcome to the Non Right Angle Trigonometry Calculator :)
You can use this program to find the following:
- Area
- Side Lengths
- Angles

Clarifications:
Capital Letters respond to Angles
Lowercase Letters respond to Sides
BE CAREFUL to ensure that the same letter in lowercase and uppercase are opposite each other.
For example, Side 'a' must be opposite Angle 'A', and so on
This will ensure accurate measuring.

NOTE: Please make sure you supply enough values for the calculations''')
def number_checker(question):
    global response
    error = "Please enter a measurement greater than 0"

    while True:
        response = input(question).lower()
        if response == '':
            return response
        try:
            response = float(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
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

#Main Routine
statement_decorator("Non Right Angle Trigonometry Calculator", "=",1)
instructions_choice = string_checker("Would you like to view the instructions?\n",["yes","no"], 1)
if instructions_choice == "yes":
    instructions()
else:
    print("Ok. Loading...")

while True:
    #Get User Goal and Perform Calculations
    goal = string_checker("What do you want to figure out? Angle, Side Length or Triangle Area?\n",options,2)
    if goal == "area":
        #Area Calculation
        a = number_checker(f"a: ")
        b = number_checker(f"b: ")
        C = number_checker(f"C: ")
        if C >= 180:
            print("That number is too large")
            continue
        triangle_area = 0.5 * a * b * math.sin(math.radians(C))
        print(f"The Area of the Triangle is {triangle_area:.2f}m^2")
    elif goal == "side length":
        #Side Length Calculation
        method = string_checker("Would you like to use the Sine or Cosine Method? ",["sine","cosine"],1)
        if method == "sine":
            a = number_checker(f"a: ")
            A = number_checker(f"A: ")
            B = number_checker(f"B: ")
            if A + B >= 180:
                print("That number is too large")
                continue
            side_length = a/math.sin(math.radians(A)) * math.sin(math.radians(B))
        else:
            b = number_checker(f"b: ")
            c = number_checker(f"c: ")
            A = number_checker(f"A: ")
            if A >= 180:
                print("That number is too large")
                continue
            side_length = b**2 + c**2 - 2 * b * c * math.cos(math.radians(A))
        print(f"The length of this side of the Triangle is {side_length:.2f}m")
    else:
        #Angle Calculations
        method = string_checker("Would you like to use the Sine or Cosine Method? ",["sine","cosine"],1)
        if method == "sine":
            a = number_checker(f"a: ")
            b = number_checker(f"b: ")
            B = number_checker(f"B: ")
            if B >= 180:
                print("That number is too large")
                continue
            angle = math.degrees(math.asin(math.sin(math.radians(B)) / b * a))
        else:
            a = number_checker(f"a: ")
            b = number_checker(f"b: ")
            c = number_checker(f"c: ")
            cos_check = b**2 + c**2 - a**2/2 * b * c
            if -1 <= cos_check <= 1:
                angle = math.degrees(math.acos(cos_check))
                #Range for Sin is also -1 to 1
            else:
                print("This Triangle is impossible. A value that falls outside the acceptable inverse cosine range of -1 to 1 is impossible")
                continue
        print(f"The size of this angle within the Triangle is {angle:.2f} degrees")

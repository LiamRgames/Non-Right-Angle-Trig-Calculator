#Importing Modules
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import numpy as np

#Definitions
response = ''
options = ["angle","side length","area"]
units = ["millimetres","centimetres","metres","kilometres","millimeters","centimeters","meters","kilometers","mm","cm","m","km"]
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
    #Reset Definitions
    a = 0
    b = 0
    c = 0
    A = 0
    B = 0
    C = 0
    graph_sides = []
    graph_angles = []
    #Get User Goal and Perform Calculations
    measurement_unit = string_checker("What unit of measurement do you want to use?\n",units, 2)
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
        print(f"The Area of the Triangle is {triangle_area:.2f} {measurement_unit}^2")
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
            side_length = b = a/math.sin(math.radians(A)) * math.sin(math.radians(B))
        else:
            b = number_checker(f"b: ")
            c = number_checker(f"c: ")
            A = number_checker(f"A: ")
            if A >= 180:
                print("That number is too large")
                continue
            side_length = a = np.sqrt(b**2 + c**2 - 2 * b * c * math.cos(math.radians(A)))
        print(f"The length of this side of the Triangle is {side_length:.2f} {measurement_unit}")
    else:
        #Angle Calculations
        method = string_checker("Would you like to use the Sine or Cosine Method? ",["sine","cosine"],1)
        if method == "sine":
            a = number_checker(f"a: ")
            b = number_checker(f"b: ")
            B = number_checker(f"B: ")
            sin_check = (math.sin(math.radians(B)) / b) * a
            if B >= 180:
                print("That number is too large")
                continue
            if -1 <= sin_check <= 1:
                angle = A = math.degrees(math.asin(sin_check))
            else:
                print("This Triangle is impossible. A value that falls outside the acceptable sine range of -1 to 1 is impossible")
                continue
        else:
            a = number_checker(f"a: ")
            b = number_checker(f"b: ")
            c = number_checker(f"c: ")
            cos_check = (b**2 + c**2 - a**2) / (2 * b * c)
            if -1 <= cos_check <= 1:
                angle = A = math.degrees(math.acos(cos_check))
            else:
                print("This Triangle is impossible. A value that falls outside the acceptable cosine range of -1 to 1 is impossible")
                continue
        print(f"The size of this angle within the Triangle is {angle:.2f} degrees")
    graph_sides.append(a)
    graph_sides.append(b)
    graph_sides.append(c)
    graph_angles.append(A)
    graph_angles.append(B)
    graph_angles.append(C)

    #Matplotlib Integration
    fig, ax = plt.subplots()
    plt.plot(-7.5, 2.5, marker='o')
    plt.plot(-2.5, 2.5, marker='o')
    plt.plot(-5, 7.5, marker='o')
    plt.plot((-7.5, -2.5, -5.0, -7.5), (2.5, 2.5, 7.5, 2.5))
    plt.title("Your Triangle")
    plt.axis('off')
    plt.annotate("A", (-7.5, 2.5), textcoords="offset points", xytext=(-10, -10))
    plt.annotate("B", (-2.5, 2.5), textcoords="offset points", xytext=(7, -10))
    plt.annotate("C", (-5, 7.5), textcoords="offset points", xytext=(0, 5))
    plt.annotate(f"Side AB: {graph_sides[2]:.2f}{measurement_unit}", (-5, 2.5), textcoords="offset points", xytext=(0, -15))
    plt.annotate(f"Side BC: {graph_sides[0]:.2f}m", (-3.75, 5), textcoords="offset points", xytext=(0, 10))
    plt.annotate(f"Side AC: {graph_sides[1]:.2f}m", (-6, 5), textcoords="offset points", xytext=(-90, 10))

    # Angle Arc Plotting
    angle_arc_A = patches.Arc(xy=(-7.5, 2.5), width=1, height=1, angle=360, theta1=0, theta2=65)
    angle_arc_B = patches.Arc(xy=(-2.5, 2.5), width=1, height=1, angle=115, theta1=0, theta2=65)
    angle_arc_C = patches.Arc(xy=(-5, 7.5), width=1, height=1, angle=245, theta1=0, theta2=55)
    ax.add_patch(angle_arc_A)
    ax.add_patch(angle_arc_B)
    ax.add_patch(angle_arc_C)
    plt.annotate(f"{graph_angles[0]:.2f}°", (-7.5, 2.5), textcoords="offset points", xytext=(30, 12))
    plt.annotate(f"{graph_angles[1]:.2f}°", (-2.5, 2.5), textcoords="offset points", xytext=(-50, 12))
    plt.annotate(f"{graph_angles[2]:.2f}°", (-5, 7.5), textcoords="offset points", xytext=(-8, -30))

    # Limits
    plt.xlim((-10, 0))
    plt.ylim((0, 10))

    # Show Graph
    plt.show()
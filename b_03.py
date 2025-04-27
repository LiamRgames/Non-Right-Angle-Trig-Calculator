#Importing Modules
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
import uuid

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

        print(f"That response is invalid, please select an option from the following:\n{",".join(map(str, answers))}")

#Main Routine
statement_decorator("Non Right Angle Trigonometry Calculator", "=",1)
instructions_choice = string_checker("Would you like to view the instructions?\n",["yes","no"], 1)
if instructions_choice == "yes":
    instructions()
else:
    print("Ok. Loading...")

while True:
    #Reset Definitions
    answer = 0
    area_variables = {"a": -1, "b": -1, "C": -1}
    sine_side_lengths = {"a": -1, "A": -1, "B": -1}
    cosine_side_lengths = {"b": -1, "c": -1, "A": -1}
    sine_angle_values = {"a": -1, "b": -1, "B": -1}
    cosine_angle_values = {"a": -1, "b": -1, "c": -1}
    graph_side_lengths = {"a": -1, "b": -1, "c": -1}
    graph_angles = {"A": -1, "B": -1, "C": -1}

    #Get User Goal and Perform Calculations
    measurement_unit = string_checker("What unit of measurement do you want to use?\n",units, 2)
    goal = string_checker("What do you want to figure out? Angle, Side Length or Triangle Area?\n",options,2)
    if goal == "area":
        #Area Calculation
        for key in area_variables.keys():
            area_variables[key] = number_checker(f"{key}: ")
            if key == key.lower():
                graph_side_lengths[key] = area_variables[key]
            else:
                graph_angles[key] = area_variables[key]

        if area_variables["C"] >= 180:
            print("That angle is too large")
            continue

        answer = 0.5 * area_variables["a"] * area_variables["b"] * math.sin(math.radians(area_variables["C"]))
        print(f"The Area of the Triangle is {answer:.2f} {measurement_unit}^2")
    elif goal == "side length":
        #Side Length Calculation
        method = string_checker("Would you like to use the Sine or Cosine Method? ",["sine","cosine"],1)
        if method == "sine":
            for key in sine_side_lengths.keys():
                sine_side_lengths[key] = number_checker(f"{key}: ")
                if key == key.lower():
                    graph_side_lengths[key] = sine_side_lengths[key]
                else:
                    graph_angles[key] = sine_side_lengths[key]
            if sine_side_lengths["A"] + sine_side_lengths["B"] >= 180:
                print("One of more of those angles is too large")
                continue

            answer = graph_side_lengths["b"] = sine_side_lengths["a"]/math.sin(math.radians(sine_side_lengths["A"])) * math.sin(math.radians(sine_side_lengths["B"]))

        else:
            #Cosine Method
            for key in cosine_side_lengths.keys():
                cosine_side_lengths[key] = number_checker(f"{key}: ")
                if key == key.lower():
                    graph_side_lengths[key] = cosine_side_lengths[key]
                else:
                    graph_angles[key] = cosine_side_lengths[key]
            if cosine_side_lengths["A"] >= 180:
                print("That angle is too large")
                continue
            answer = graph_side_lengths["a"] = np.sqrt(cosine_side_lengths["b"]**2 + cosine_side_lengths["c"]**2 - 2 * cosine_side_lengths["b"] * cosine_side_lengths["c"] * math.cos(math.radians(cosine_side_lengths["A"])))
        print(f"The length of this side of the Triangle is {answer:.2f}{measurement_unit}")
    else:
        #Angle Calculations
        method = string_checker("Would you like to use the Sine or Cosine Method? ",["sine","cosine"],1)
        if method == "sine":
            for key in sine_angle_values.keys():
                sine_angle_values[key] = number_checker(f"{key}: ")
                if key == key.lower():
                    graph_side_lengths[key] = sine_angle_values[key]
                else:
                    graph_angles[key] = sine_angle_values[key]
            sin_check = (math.sin(math.radians(sine_angle_values["B"])) / sine_angle_values["b"]) * sine_angle_values["a"]
            if sine_angle_values["B"] >= 180:
                print("That angle is too large")
                continue
            elif -1 <= sin_check <= 1:
                answer = graph_angles["A"] = math.degrees(math.asin(sin_check))
            else:
                print("This Triangle is impossible. A value that falls outside the acceptable sine range of -1 to 1 is impossible")
                continue
        else:
            #Cosine Method
            for key in cosine_angle_values.keys():
                cosine_angle_values[key] = number_checker(f"{key}: ")
                if key == key.lower():
                    graph_side_lengths[key] = cosine_angle_values[key]
                else:
                    graph_angles[key] = cosine_angle_values[key]
            cos_check = (cosine_angle_values["b"]**2 + cosine_angle_values["c"]**2 - cosine_angle_values["a"]**2) / (2 * cosine_angle_values["b"] * cosine_angle_values["c"])
            if -1 <= cos_check <= 1:
                answer = graph_angles["A"] = math.degrees(math.acos(cos_check))
            else:
                print("This Triangle is impossible. A value that falls outside the acceptable cosine range of -1 to 1 is impossible")
                continue
        print(f"The size of this angle within the Triangle is {answer:.2f} degrees")

    #Matplotlib Integration
    fig, ax = plt.subplots()
    plt.plot(-7.5, 2.5, marker='o')
    plt.plot(-2.5, 2.5, marker='o')
    plt.plot(-5, 7.5, marker='o')
    plt.plot((-7.5, -2.5, -5.0, -7.5), (2.5, 2.5, 7.5, 2.5))
    plt.title("Your Triangle (Not to Scale)")
    plt.axis('off')
    plt.annotate("A", (-7.5, 2.5), textcoords="offset points", xytext=(-10, -10))
    plt.annotate("B", (-2.5, 2.5), textcoords="offset points", xytext=(7, -10))
    plt.annotate("C", (-5, 7.5), textcoords="offset points", xytext=(0, 5))
    if graph_side_lengths["c"] != -1:
        plt.annotate(f"Side AB: {graph_side_lengths["c"]:.2f}{measurement_unit}", (-5, 2.5), textcoords="offset points", xytext=(0, -15))
    if graph_side_lengths["a"] != -1:
        plt.annotate(f"Side BC: {graph_side_lengths["a"]:.2f}{measurement_unit}", (-3.75, 5), textcoords="offset points", xytext=(0, 10))
    if graph_side_lengths["b"] != -1:
        plt.annotate(f"Side AC: {graph_side_lengths["b"]:.2f}{measurement_unit}", (-6, 5), textcoords="offset points", xytext=(-90, 10))

    # Angle Arc Plotting
    angle_arc_A = patches.Arc(xy=(-7.5, 2.5), width=1, height=1, angle=360, theta1=0, theta2=65)
    angle_arc_B = patches.Arc(xy=(-2.5, 2.5), width=1, height=1, angle=115, theta1=0, theta2=65)
    angle_arc_C = patches.Arc(xy=(-5, 7.5), width=1, height=1, angle=245, theta1=0, theta2=55)
    ax.add_patch(angle_arc_A)
    ax.add_patch(angle_arc_B)
    ax.add_patch(angle_arc_C)
    if graph_angles["A"] != -1:
        plt.annotate(f"{graph_angles["A"]:.1f}°", (-7.5, 2.5), textcoords="offset points", xytext=(30, 12))
    if graph_angles["B"] != -1:
        plt.annotate(f"{graph_angles["B"]:.1f}°", (-2.5, 2.5), textcoords="offset points", xytext=(-50, 12))
    if graph_angles["C"] != -1:
        plt.annotate(f"{graph_angles["C"]:.1f}°", (-5, 7.5), textcoords="offset points", xytext=(-8, -30))

    # Limits
    plt.xlim((-10, 0))
    plt.ylim((0, 10))

    #Unique File Name Generation
    unique_file_name = f"{str(uuid.uuid4())}.png"

    #Show and Save Graph
    plt.savefig(unique_file_name)
    plt.show()

    #Removing Unnecessary Values for File History Update
    for i in list(graph_side_lengths.keys()):
        if graph_side_lengths[i] == -1:
            del graph_side_lengths[i]
    for i in list(graph_angles.keys()):
        if graph_angles[i] == -1:
            del graph_angles[i]

    #Link to plot
    html_plot_view = f'<a href="{unique_file_name}">View Plot</a>'

    #File Information
    file_name = "Non_Right_Angle_Trigonometry_Calculator_History"
    file_path = "{}.html".format(file_name)

    answer = f"{answer:.2f}"

    #Writing to File
    try:
        with open(file_path, "r"):
            created = True
    except FileNotFoundError:
        created = False

    with open(file_path, "a+") as text_file:
        if not created:
            text_file.write("<h2>Non Right Angle Trigonometry Calculator History</h2>")
        text_file.write("<table border='1'><tr><th>Sides</th><th>Values</th>")
        for key, value in graph_side_lengths.items():
            text_file.write(f"<tr><td>{key}</td><td>{value:.2f}</td></tr>")
        text_file.write("</table><br>")

        text_file.write("<table border='1'><tr><th>Angles</th><th>Values</th>")
        for key, value in graph_angles.items():
            text_file.write(f"<tr><td>{key}</td><td>{value:.2f}</td></tr>")
        text_file.write("</table><br>")
        if goal == "area":
            text_file.write(f"Answer: {answer}{measurement_unit}^2<br>")
        else:
            text_file.write(f"Answer: {answer}{measurement_unit}<br>")
        text_file.write(html_plot_view)
        text_file.write("<hr>")
        print("Your Calculation History File has been updated")
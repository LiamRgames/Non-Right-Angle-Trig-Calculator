#Definitions
sides = {"a": 99, "b": -1, "c": 55}
angles = {"A": 45, "B": 102, "C": -1}
answer = 5
unit_of_measurement = "m^2"

#Removing Unnecessary Values
for i in list(sides.keys()):
    if sides[i] == -1:
        del sides[i]
for i in list(angles.keys()):
    if angles[i] == -1:
        del angles[i]

#Link to Integrate into Base Version
html_plot_view = '<a href="plot.png">View Plot</a>'

#File Information
file_name = "Non_Right_Angle_Trigonometry_Calculator_History"
file_path = "{}.html".format(file_name)

#Writing to File
try:
    with open(file_path, "r"):
        created = True
except FileNotFoundError:
    created = False

with open(file_path,"a+") as text_file:
    if not created:
        print("Your Calculation History File has been updated")
        text_file.write("<h2>Non Right Angle Trigonometry Calculator History</h2>")
    text_file.write("<table border='1'><tr><th>Sides</th><th>Values</th>")
    for key,value in sides.items():
        text_file.write(f"<tr><td>{key}</td><td>{value}</td></tr>")
    text_file.write("</table><br>")

    text_file.write("<table border='1'><tr><th>Angles</th><th>Values</th>")
    for key,value in angles.items():
        text_file.write(f"<tr><td>{key}</td><td>{value}</td></tr>")
    text_file.write("</table><br>")

    text_file.write(f"Answer: {str(answer)}{unit_of_measurement}\n<br>")
    text_file.write(html_plot_view)
    text_file.write("<hr>")


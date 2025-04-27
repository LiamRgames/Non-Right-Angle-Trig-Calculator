import pandas

sides = {"a": -1, "b": 80, "c": 40}
angles = {"A": 120, "B": 20, "C": -1}
answer = 5
unit_of_measurement = "m^2"
html_plot_view = '<a href="plot.png">View Plot</a>'

#Removing Empty Values
for i in sides.keys():
    if i == -1:
        delete = sides.pop(i)
for i in angles.keys():
    if i == -1:
        delete = angles.pop(i)
s_dict = {"Sides": sides}
a_dict = {"Angles": angles}

#Pandas Display
frame = pandas.DataFrame(s_dict)
frame2 = pandas.DataFrame(a_dict)

#File Information
file_name = "Non_Right_Angle_Trigonometry_Calculator_History"
file_path = "{}.html".format(file_name)
text_file = open(file_path, "a+")

#Write to file
text_file.write(str(frame))
text_file.write("\n")
text_file.write(str(frame2))
text_file.write("\n")
text_file.write(f"Answer: {str(answer)}{unit_of_measurement}\n")
text_file.write(html_plot_view)


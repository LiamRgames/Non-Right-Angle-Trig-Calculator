import pandas
sides = {"a":-1, "b":-1,"c":-1}
angles = {"A":-1, "B":-1,"C":-1}
s_dict = {"Sides": sides}
a_dict = {"Angles": angles}
answer = 5
unit_of_measurement = "m^2"

frame = pandas.DataFrame(s_dict)
frame2 = pandas.DataFrame(a_dict)

print(f"{frame}\n{frame2}")
print(f"Answer: {answer}{unit_of_measurement}")
import pandas
sides = {"a":-1, "b":25,"c":90}
angles = {"A":50, "B":-1,"C":-1}
dictionary = {
    "Sides": sides,
    "Angles": angles
}

frame = pandas.DataFrame(dictionary)

print(frame)

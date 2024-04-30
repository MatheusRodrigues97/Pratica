studentes = []

with open("names.csv", "r") as file:
    for line in file:
         name, house = line.rstrip().split(",")
         studente = {"name":name, "house":house}
         studentes.append(studente)

for student in sorted(studentes, key = lambda student: student["name"]):
     print(f"{student['name']} is in {student['house']}")
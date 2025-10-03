person = {
    "Name": "Valentin",
    "Age": 21,
    "City": "Rouhling"
    }

person["Occupation"] = "Sales"
person.update({"Age": 22})
person.pop("City")

print(person)
print(type(person))

person.get(21)

print(person)

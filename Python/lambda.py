people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Darco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)
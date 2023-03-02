
# dictionary inside a list
people = [
    {"name": "Harry", "house": "Covid St"},
    {"name": "Amy", "house": "Zel St"},
    {"name": "Celci", "house": "High St"}
]

###### sort by house #####
#return house
def f(person):
    return person["house"]
#sort by key = house
people.sort(key=f)
print(">>>>>>>Sort by house---------------")
print(people)


######sort people by name #####
def f(person):
    return person["name"]
people.sort(key=f)
print(">>>>>>sort by name--------------")
print(people)

#### LAMBDA EXPRESSION : include a function as a single value on a single line #####
# key = lambda 
#input: person
#output: person["name"]
people.sort(key = lambda person: person["name"])
print(">>>>>Sort by name using LAMBDA EXPRESSION ----------------")
print(people)
            
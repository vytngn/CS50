# Create an empty set 
s = set()

# Add elements to set, element less than 6
for x in range(6):
    s.add(x)

# add duplicate element 1 to the set --> only one will be recognized
s.add(1)
print("Duplicate element 1 is added")
print(s)
print("------------------")

# add 10
s.add(10)
print("10 is added")
print(s)
print("------------------")
# remove 2
s.remove(2)
print("2 has been removed")
print(s)
print("------------------")

# get length of the set (how many elements)
length = len(s)
print(f"The set has total of {length} elements.")
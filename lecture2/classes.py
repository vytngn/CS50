################# OBJECT ORIENTED PROGRAMMING ################
#define a new aclass 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y 

p = Point(2,8)
print(p.x)
print(p.y)

class Flight():

    #method to create a class
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    #method to add passenger to the flight
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    #method return open seat in a flight 
    def open_seats(self):
        return self.capacity - len(self.passengers)


#flight capacity of 3
flight = Flight(3)
people = ["Susane","Alfie", "Kem","Sunny","Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to the flight successfully")
    else:
        print(f"No available seat for {person}")



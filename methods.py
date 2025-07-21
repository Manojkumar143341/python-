class Vehicle:
    def run(self):
        print("Vehicle is running")

class Car(Vehicle):
    def run(self):
        print("Car is running smoothly")

c = Car()
c.run()

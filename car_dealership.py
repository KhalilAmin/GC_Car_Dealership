class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        engine_on = False
    def start_engine(self):
        print("Starting engine...")
        engine_on = True
    def make_noise(self):
        print("Beep Beep!")
class Truck(Vehicle):
    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        cargo = False
    def load_cargo(self):
        print("Loading the truck bed...")
        cargo = True

class Motorcycle(Vehicle):
    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
    def make_noise(self):
        print("Vroom Vroom!")

trucks = [Truck("Toyota", 15000, 25000), Truck("Ford", 150000, 5000), Truck("Dodge", 5000, 36000)]
bikes = [Motorcycle("Suzuki", 12000, 3000), Motorcycle("Yamaha", 180, 18000), Motorcycle("Honda", 1500, 12000)]
compare_list = []

print("Hello!")
print("Welcome to KAL Bikes and Trucks!")
running = True
while running:
    choiceInput = input("Would you like to view Bikes or Trucks? (B or T): ").lower()
    if choiceInput == "t":
        for i in trucks:
            print(f'{i.make}: with {i.miles} miles, costs ${i.price}')
        running = False

    elif choiceInput =="b":
        for i in bikes:
            print(f'{i.make}: with {i.miles} miles, costs ${i.price}')
        running = False

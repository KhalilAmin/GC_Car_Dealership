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

trucks = [Truck("Toyota", 15000, 25000),
          Truck("Ford", 150000, 5000),
          Truck("Dodge", 5000, 36000)]

bikes = [Motorcycle("Suzuki", 12000, 3000),
         Motorcycle("Yamaha", 180, 18000),
         Motorcycle("Honda", 1500, 12000)]

vehicles_to_compare = []

print("Hello!")
print("Welcome to KAL Bikes and Trucks!")
running = True
while running:
    choiceInput = input("Would you like to view Bikes or Trucks? (B or T):\n> ").lower()
    if choiceInput == "t":
        for truck in trucks:
            print(f'{trucks.index(truck)+1}. {truck.make}: with {truck.miles} miles costs ${truck.price}')
        compare = input("Would you like to compare one of these vehicles today? (y or n)\n> ").lower()
        if compare == "y":
            compareChoice = int(input("Which vehicle would you like to compare? (Please list numer)\1> ")) - 1
            vehicles_to_compare.append[trucks[compareChoice]]
            print(f'{trucks[compareChoice].make} added!')

    elif choiceInput =="b":
        for bike in bikes:
            print(f'{bikes.index(bike)+1}. {bike.make}: with {bike.miles} miles costs ${bike.price}')
        compare = input("Would you like to compare one of these vehicles today? (y or n)\n> ")
        if compare == "y":
            compareChoice = int(input("Which vehicle would you like to compare? (Please list numer)\1> ")) - 1
            vehicles_to_compare.append[bikes[compareChoice]]
            print(f'{bikes[compareChoice].make} added!')

    else:
        print("Invalid choice. Please enter 'b' or 't'. ")

    compare_now = input("Would you like to compare your vehicles now? (y or n) ").lower()
    if compare_now == "y":
        print("Here are your vehicles to compare:")
        for vehicle in vehicles_to_compare:
            print(f"{vehicle.make}: with {vehicle.miles} miles costs ${vehicle.price}")
            vehicle.make_noise()

        print("Thank you and have a nice day!")
        break

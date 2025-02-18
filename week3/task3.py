class Vehicle:
    def __init__(self,make,model):
        self._make= make
        self._model = model

    def get_make(self):
        return self._make
    def get_model(self):
        return self._model
    def set_make(self, make):
        self._make = make
    def set_model(self, model):
        self._model = model
    def describe(self):
        return f"This is a vVehicle. Male:{self._make}, Model: {self._model}"


class Car(Vehicle):
    def __init__(self, make,model,num_doors):
        super().__init__(make,model)
        self.num_doors = num_doors
    def describe(self):
        return f"This is a car. Make: {self.get_make()}, Model: {self.get_model()}, Doors: {self.num_doors}"

class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)  
        self.bike_type = bike_type 
    def describe(self):
        return f"This is a bike. Make: {self.get_make()}, Model: {self.get_model()}, Type: {self.bike_type}"



# Polymorphism in action:
def vehicle_describe(vehicle):
    print(vehicle.describe())

# Create instances of Car and Bike
car = Car("Toyota", "Vitz", 4)
bike = Bike("Mountain", "AA-1", "normal")

# Calling the same describe method, but the output will be different based on the object type
vehicle_describe(car)  
vehicle_describe(bike)  



    

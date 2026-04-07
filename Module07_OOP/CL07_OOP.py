### This template is for the class demo and exercises covered in M07_Lec12_oop for CS 22B.

class Car:
    ## Initializer method - set up the attributes for Car class
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def get_description(self):
        '''Instance method that returns a string description of the car.'''
        # return f"The {self.make} {self.model} is a {self.color} color."  
        return "The {} {} is a {} color.".format(self.make, self.model, self.color)

## Instantiate a Car object. Instance attributes 
toyota_camry = Car("Toyota", "Camry", "blue")
honda_civic = Car("Honda", "Civic", "silver")

## Call our instance method
print(toyota_camry.get_description())
print(honda_civic.get_description())

### Child class that inherits from Car
class GasCar(Car):
    def __init__(self, make, model, color, fuel_tank_size):
        super().__init__(make, model, color)  # Call the initializer of the parent class
        self.fuel_tank_size = fuel_tank_size  # New attribute specific to GasCar

    def get_fuel_tank_info(self):
        '''Instance method that returns a string description of the fuel tank.'''
        return "The {} {} has a {} gallon fuel tank.".format(self.make, self.model, self.fuel_tank_size)

class ElectricCar(Car):
    def __init__(self, make, model, color, battery_size):
        super().__init__(make, model, color)  # Call the initializer of the parent class
        self.battery_size = battery_size  # New attribute specific to ElectricCar

    def get_battery_info(self):
        '''Instance method that returns a string description of the battery.'''
        return "The {} {} has a {} kWh battery.".format(self.make, self.model, self.battery_size)

class HybridCar(Car):
    def __init__(self, make, model, color, fuel_efficiency):
        super().__init__(make, model, color)  # Call the initializer of the parent class
        self.fuel_efficiency = fuel_efficiency  # New attribute specific to HybridCar

    def get_fuel_efficiency_info(self):
        '''Instance method that returns a string description of the fuel efficiency.'''
        return "The {} {} has a fuel efficiency of {} MPG.".format(self.make, self.model, self.fuel_efficiency) 
 
### Example usage of child classes
gas_car = GasCar("Ford", "Mustang", "red", 16)
print(gas_car.get_description())
# print(gas_car.get_fuel_tank_info())

##### Example of superclass and subclass ####
## We will create a class called Circle that has 
# attribute radius
# methods area() and circumference()   

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        area = 3.14 * self.radius ** 2
        return area
    
    def circumference(self):
        circumference = 2 * 3.14 * self.radius
        return circumference
    
## Use case: Create an instance of the Circle class and call the area and circumference methods to verify that they work correctly.
my_circle = Circle(5)
print("Area of the circle:", my_circle.area())
print("Circumference of the circle:", my_circle.circumference())
class Car():
    def __init__(self, make, model, year):
        """initializing attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Car description"""
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """odometer info"""
        print(f"This car, done distance of {self.odometer_reading} km")

    def update_odometer(self, milage):
        """add value to odometer"""
        self.odometer_reading = milage

    def increment_odometer(self, kilometers):
        """incrementation"""
        self.odometer_reading += kilometers

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print(f"Ten samochod ma baterie o pojemnosci {self.battery_size} kWh.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23 #modification with no metod
my_new_car.read_odometer()

my_new_car.update_odometer(23) #modification with metod
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(2000000)
my_used_car.read_odometer()

my_used_car.increment_odometer(10000)
my_used_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
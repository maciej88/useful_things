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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
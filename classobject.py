class Gari:
    def __init__(self, make , model , year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_gari(self):
        return f"The {self.make} {self.model} {self.year}"
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles"
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
my_gari = Gari("Ford", "Horsepower",2019)

print(my_gari.describe_gari())
print(my_gari.read_odometer())
my_gari.update_odometer(100)
print(my_gari.odometer_reading)
my_gari.increment_odometer(50)
print(my_gari.read_odometer())
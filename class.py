class Cars:
    def __init__(self, make, model, year, color): #firstfunction
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def describe_car(self):
        print(f"My dream car is {self.make} and my model is {self.model} manufactured in {self.year} and is {self.color} in color.")

my_car = Cars("Ford", "Corn", "2016", "Black")

my_car.describe_car()#calling the funtion
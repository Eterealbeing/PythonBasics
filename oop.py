class Fruits:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe_fruits(self):
        print(f"I love eating {self.name} and it costs Kshs.{self.price}.")

my_fruits = Fruits("Apple", 50)
my_fruits.describe_fruits()

my_fruits1 = Fruits("Grapes", 500)
my_fruits1.describe_fruits()

my_fruits2 = Fruits("Melons", 200)
my_fruits2.describe_fruits()

my_fruits3 = Fruits("Bananas", 10)
my_fruits3.describe_fruits()

my_fruits4 = Fruits("Guavas", 30)
my_fruits4.describe_fruits()


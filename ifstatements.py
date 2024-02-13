nambari = int(input("Enter Number:"))

if nambari % 2 == 0:
    print(f"{nambari} is even number")
else:
    print(f"{nambari} is odd number")

age = int(input("Enter Age:"))

if 18 >= age < 100:
    print("You can vote")
else:
    print("You cannot vote")

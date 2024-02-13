weight = float(input("What is your weight in Kg? "))
height = float(input("What is your height in Metres? "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    result = "Underweight"

elif 18.5 <= bmi < 25:
    result = "Normal"

elif 25 <= bmi < 30:
    result = "Overweight"

else:
    result = "Obese"

print(f"Your BMI is {bmi:.2f} and you are classified as {result}")

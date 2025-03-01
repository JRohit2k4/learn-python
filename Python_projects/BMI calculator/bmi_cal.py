# BMI Calculator

# Taking user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight / (height ** 2)

# Categorizing BMI
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Displaying the result
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")


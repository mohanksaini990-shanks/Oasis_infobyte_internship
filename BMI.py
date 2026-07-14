# BMI Calculator
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
if weight <= 0 or height <= 0:
    print("Please enter valid values!")
        
bmi = weight / (height * height)

print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
# Basic BMI Calculator
def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI using formula: BMI = weight / (height^2)
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate and display
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")

# BMI Calculator with Categories
def calculate_bmi(weight_kg, height_m):
    """Calculate BMI"""
    return weight_kg / (height_m ** 2)

def get_bmi_category(bmi):
    """Determine BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate
bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

# Display results
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")
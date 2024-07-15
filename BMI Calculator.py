def calculate_bmi(height, weight):
    # BMI formula: weight (kg) / height (m)^2
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif bmi >= 30:
        return "Obesity"
    else:
        return "Invalid BMI"

def main():
    try:
        height = float(input("Enter your height in meters (e.g., 1.75): "))
        weight = float(input("Enter your weight in kilograms (e.g., 68): "))

        bmi = calculate_bmi(height, weight)
        category = bmi_category(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are in the category of: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values for height and weight.")

if __name__ == "__main__":
    main()




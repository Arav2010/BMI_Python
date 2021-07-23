weight = int(input("Please enter your Weight: "))
height = float(input("Please enter your Height: "))

bmi = int(weight / (height * height))

print("Calculating your BMI...")

print("Your BMI is", bmi)

if (bmi <= 18):
    print("You are Underweight")
elif (bmi >= 23):
    print("You are Overweight")
else:
    print("You are absolutely Fit")

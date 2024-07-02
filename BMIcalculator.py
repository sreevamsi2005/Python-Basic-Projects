# Ask the user to input their height in centimeters
Height = float(input("Enter your height in centimeters: "))

# Ask the user to input their weight in kilograms
Weight = float(input("Enter your Weight in Kg: "))

# Convert the height from centimeters to meters by dividing by 100
Height = Height / 100

# Calculate the Body Mass Index (BMI) by dividing the weight by the square of the height
BMI = Weight / (Height * Height)

# Print the calculated BMI
print("your Body Mass Index is: ", BMI)

# Check if the BMI is a positive value (i.e., the user entered valid details)
if (BMI > 0):
  # Check the BMI category and print the corresponding message
  if (BMI <= 16):
    print("you are severely underweight")
  elif (BMI <= 18.5):
    print("you are underweight")
  elif (BMI <= 25):
    print("you are Healthy")
  elif (BMI <= 30):
    print("you are overweight")
  else:
    print("you are severely overweight")
else:
  # If the BMI is not a positive value, print an error message
  print("enter valid details")


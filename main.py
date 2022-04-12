# BMI 2.0 
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# underweght, normal_weight, overweight, obese, clinically obese
body_mass_index = weight / height**2 
# example: 85 / 1,75 * 1,75 = 27,75 BMI
if body_mass_index <= 18.5:
  print("Your BMI is body_mass_index. You are underweight!")
else:
  print("Your BMI is body_mass_index. You have normal weight!")
  
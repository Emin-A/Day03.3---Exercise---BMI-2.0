# BMI 2.0 
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# underweght, normal_weight, overweight, obese, clinically obese
body_mass_index = weight / height**2 
# example: 85 / 1,75 * 1,75 = 27,75 BMI
if body_mass_index <= 18.5:
  print("Your BMI is {:0.2f}.".format(body_mass_index) + " You are underweight!") 
else:
  if body_mass_index <= 25.0:
    print("Your BMI is {:0.2f}.".format(body_mass_index) + " You have normal weight!")
  else:
      if body_mass_index <= 30.0:
        print("Your BMI is {:0.2f}.".format(body_mass_index) + " You are overweight!")
      else:
          if body_mass_index <= 35:
            print("Your BMI is {:0.2f}.".format(body_mass_index) + " You are obese!")
          else:
              if body_mass_index > 35:
                print("Your BMI is {:0.2f}.".format(body_mass_index) + " You are clinically obese!")
# else:
#   print("Your BMI is {:0.2f}.".format(body_mass_index) + " You have normal weight!")
  

# if body_mass_index <= 18.5:
#   print("Your BMI is {:0.2f}.".format(body_mass_index) + " You are underweight!") 
# elif body_mass_index > 18.5:
#   print("Your BMI is {:0.2f}.".format(body_mass_index) + " You have normal weight!")
# elif body_mass_index > 25.0:
#   print("Your BMI is {:0.2f}.".format(body_mass_index) + " You are overweight!")
# elif body_mass_index > 30:
#   print("Your BMI is {:0.2f}.".format(body_mass_index) + " You are obese!")
# elif body_mass_index >= 35:
#   print("Your BMI is {:0.2f}.".format(body_mass_index) + " You are clinically obese!")
# else:
#   print("Your BMI is {:0.2f}.".format(body_mass_index) + " You have normal weight!")
  
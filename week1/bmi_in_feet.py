weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in feet: "))

height = height * 0.3048  

bmi = weight / (height ** 2)

print("This is BMI:", round(bmi, 2))

if bmi < 18.5:
    print("You are under weight")
elif bmi < 25:
    print("You r normal")
elif bmi < 30:
    print("You r over weight")
else:
    print("You are obese")

def calculator():
    num1 = float(input("Enter Number 1: "))
    oper = input("Enter an operator (+,-,*,/,<,>)")
    num2 = float(input("Enter Number 2: "))
    
    if   oper == '+':
     print(num1 + num2)
    elif oper == '-':
     print(num1 - num2)
    elif oper == '*':
     print(num1 * num2)
    elif oper == '/':
     print(num1 / num2)
    elif oper == '>':
     print(num1 > num2)
    elif oper == '<':
     print(num1 < num2)
    else:
        
     print("Invalid operator")

def Bmi():
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
       

def temperature():
    faren = float(input("Enter faren: " ))
    celsius = (faren - 32) * 5/9
    
    print("Celsius is ",celsius)
    
    if (celsius > 40):
    
        print("Temperature is hot today")
    
    elif (celsius > 50):
    
        print("Its extremely hot today")
    
    elif (celsius <0):
    
        print("Its freezing today")
    
    
    #-----------manu
print("Press 1 for Calculator")
print("Press 2 for Bmi")
print("Press 3 for temperature")

choice = input("Enter your choice")
    
if  choice == '1':

    calculator()
       
elif choice == '2':
        
    Bmi()
        
elif choice == '3':
        
    temperature()
    


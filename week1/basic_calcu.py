num1 = float(input("Enter Number 1: "))
oper = input("Enter an operator (+,-,*,/,<,>)")
num2 = float(input("Enter Number 2: "))
if (oper == '+'):
    print(num1 + num2)
elif (oper == '-'):
    print(num1 - num2)
elif (oper == '*'):
    print(num1 * num2)
elif (oper == '/'):
    print(num1 / num2)
elif (oper == '>'):
    print(num1 > num2)
elif (oper == '<'):
    print(num1 < num2)
else:
    print("Invalid operator")


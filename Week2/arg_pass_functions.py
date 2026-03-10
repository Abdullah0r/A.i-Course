def cal(num1,num2,oper):
    
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
cal(50,23,'+')

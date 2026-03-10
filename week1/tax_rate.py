sal = float(input("Enter Employee Salary: "))
if sal <= 5000:
    tax = sal * 0.02
    print("Your salary after tax is: ",tax)
if sal <= 10000:
    tax = sal * 0.04
    print("Your salary after tax is: ",tax)
elif sal >= 15000:
    tax = sal * 0.10
    print("Your salary after tax is: ",tax)
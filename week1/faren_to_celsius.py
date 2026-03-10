faren = float(input("Enter faren: " ))
celsius = (faren - 32) * 5/9
print("Celsius is ",celsius)
if (celsius > 40):
    print("Temperature is hot today",)
elif (celsius > 50):
    print("Its extremely hot today")
elif (celsius <0):
    print("Its freezing today")
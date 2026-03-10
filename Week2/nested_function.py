def greet_user(name):
    def greet():
        return f"hello ,{name}!"
    return greet()
print(greet_user("ubaid sheikh"))
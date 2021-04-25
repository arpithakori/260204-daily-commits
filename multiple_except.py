try:
    variable = 10
    print(variable + "Hello")
    print(variable/2)
except ZeroDivisionError:
    print("Error : Division by zero is not possible")
except (TypeError, ValueError):
    print("Error!!!!")

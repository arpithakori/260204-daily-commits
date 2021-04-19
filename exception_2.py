try:
    variable = 10
    print(str(variable) + "hello")
    print(variable/2)

except ZeroDivisionError:
    print("Divide by zero")

except (ValueError, TypeError):
    print("Error")

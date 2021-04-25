try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Error : Cant divide by zero")
finally:
    print("This line prints no matter what")

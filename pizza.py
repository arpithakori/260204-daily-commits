num_pizza_slices = int(input("Enter the number of pizza slices you want :\n"))
if num_pizza_slices % 2 == 0:
    print("Price per slice is Rs 120")
    price = num_pizza_slices * 120
    print(price)
else:
    print("Price per slice is Rs 123")
    price = num_pizza_slices * 123
    print(price)

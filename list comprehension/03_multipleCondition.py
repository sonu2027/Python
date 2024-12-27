numbers = [1, 2, 3, 4, 5]
squared_even_numbers = [x**2 for x in numbers if x % 2 == 0 and x > 2]
print(squared_even_numbers)  # Output: [16]
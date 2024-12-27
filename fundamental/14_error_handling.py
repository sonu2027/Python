# 1. Basic Try-Except:
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")

# 2. Try-Except with Multiple Exceptions:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
    
# 3. Finally Block:
# The finally block will always execute, whether or not an exception occurred.
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input!")
finally:
    print("This will always execute.")

# Write a Python program that Creates a list of 5 numbers. Finds and prints the largest number in the list.

number=[3,2,4,7,0]
largest=number[0]
for i in number:
    if(i>largest):
        largest=i

print("Largest number is: ", largest)